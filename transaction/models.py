from django.db import models
from django.db.models import Sum
from customer.models import customer
from inventory.models import item


class item_Transaction(models.Model):
    t_id = models.AutoField("Item Transaction ID", primary_key=True)
    i_id = models.ForeignKey(
        item, on_delete=models.CASCADE, verbose_name="Item")
    type = models.CharField("Transaction Type", choices={
        ('IN', 'IN'),
        ('OUT', 'OUT')}, max_length=3)
    quantity = models.PositiveIntegerField("Quantity")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.i_id.name

    # def add_quantity(self, quantity):
    #     item.quantity = item.quantity + quantity
    #     item.save()
    #     item_Transaction.objects.create(
    #         i_id=self.i_id, type='IN', quantity=quantity)

    def sub_quantity(self, quantity):
        item.quantity = item.quantity - quantity
        item.save()
        item_Transaction.objects.create(
            i_id=self.i_id, type='OUT', quantity=quantity)


class cust_Transaction(models.Model):
    t_id = models.AutoField("Transaction ID", primary_key=True)
    c_id = models.ForeignKey(
        customer, on_delete=models.CASCADE, verbose_name="Customer")
    total_amt = models.DecimalField(
        "Total Amount", max_digits=10, decimal_places=2, default=0)
    paid_amt = models.DecimalField(
        "Paid Amount", max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(
        "Balance Amount", max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Customer_Transaction'
        ordering = ['-created_at']

    def __str__(self):
        return self.c_id.name

    def update_balance(self):
        self.balance = self.total_amt - self.paid_amt

    def update_total_amt(self):
        total = TransactionItem.objects.filter(
            transaction=self).aggregate(Sum('price'))
        self.total_amt = total['price__sum']
        self.save()

    def save(self, *args, **kwargs):
        self.update_balance()
        super().save(*args, **kwargs)


class TransactionItem(models.Model):
    t_id = models.AutoField("Transaction Item ID", primary_key=True)
    transaction = models.ForeignKey(
        cust_Transaction, on_delete=models.CASCADE, verbose_name="Transaction")
    items = models.ForeignKey(
        item, on_delete=models.CASCADE, verbose_name="Items")
    quantity = models.PositiveIntegerField("Quantity")
    price = models.DecimalField(
        "Price", max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'transaction_item'

    def __str__(self):
        return f"{self.quantity} of {self.items.name} in transaction of {self.transaction.c_id.name} in Trans {self.transaction.t_id}"

    def save(self, *args, **kwargs):
        self.Price = self.items.price * self.quantity
        super().save(*args, **kwargs)
        self.transaction.update_total_amt()
        self.transaction.update_balance()
        item_Transaction.sub_quantity(self.items, self.quantity)
