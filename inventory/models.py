from django.db import models

# Create your models here.
choice = {
    ('IN', 'IN'),
    ('OUT', 'OUT'),
}


class item(models.Model):
    i_id = models.AutoField("Item ID", primary_key=True)
    name = models.CharField("Item Name", max_length=100)
    quantity = models.PositiveIntegerField("Quantity")
    price = models.DecimalField("Price", max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def add_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        item_Transaction.objects.create(
            i_id=self, type='IN', quantity=self.quantity)
        item_Transaction.save(self)

    def sub_quantity(self, quantity):
        self.quantity = self.quantity - quantity
        item_Transaction.objects.create(
            i_id=self, type='OUT', quantity=quantity)
        item_Transaction.save(self)


class item_Transaction(models.Model):
    t_id = models.AutoField("Item Transaction ID", primary_key=True)
    i_id = models.ForeignKey(
        item, on_delete=models.CASCADE, verbose_name="Item")
    type = models.CharField("Transaction Type", choices=choice, max_length=3)
    quantity = models.PositiveIntegerField("Quantity")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.i_id.name
