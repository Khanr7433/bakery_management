from django.db import models
from inventory.models import item
from django.db.models import Sum

# Create your models here.


class customer(models.Model):
    c_id = models.AutoField("Customer ID", primary_key=True)
    name = models.CharField("Customer Name", max_length=100)
    phone = models.CharField("Customer Phone", max_length=10)
    address = models.CharField("Customer Address", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customer'
        ordering = ['c_id']

    def __str__(self):
        return self.name


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
            transaction=self).aggregate(Sum('Price'))
        self.total_amt = total['Price__sum']
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
    Price = models.DecimalField(
        "Price", max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'transaction_item'

    def __str__(self):
        return f"{self.quantity} of {self.items.name} in transaction of {self.transaction.c_id.name} in Trans {self.transaction.t_id}"

    def save(self, *args, **kwargs):
        self.Price = self.items.price * self.quantity
        super().save(*args, **kwargs)
        self.transaction.update_total_amt()
        self.transaction.update_balance()
        # self.items.update_quantity(self.quantity)
        # self.items.add_quantity(self.quantity)
        self.items.sub_quantity(self.quantity)
