from django.contrib import admin
from customer.models import customer, cust_Transaction, TransactionItem

# Register your models here.

admin.site.register(customer)
admin.site.register(cust_Transaction)
admin.site.register(TransactionItem)
