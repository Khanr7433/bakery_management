from django.db import models


class item(models.Model):
    i_id = models.AutoField("Item ID", primary_key=True)
    name = models.CharField("Item Name", max_length=100)
    quantity = models.PositiveIntegerField("Quantity")
    price = models.DecimalField("Price", max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['i_id']

    def __str__(self):
        return self.name
