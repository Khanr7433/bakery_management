from django.db import models


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
