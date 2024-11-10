from django.contrib import admin
from customer.models import customer, cust_Transaction, TransactionItem

# Register your models here.


class customerAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'name', 'address', 'phone')
    search_fields = ('c_id', 'name', 'address', 'phone')
    list_filter = ('c_id', 'name', 'address', 'phone')


class cust_TransactionAdmin(admin.ModelAdmin):
    list_display = ('t_id', 'c_id', 'total_amt', 'paid_amt', 'balance')
    search_fields = ('t_id', 'c_id', 'total_amt', 'paid_amt', 'balance')
    list_filter = ('t_id', 'c_id', 'total_amt', 'paid_amt', 'balance')


class TransactionItemAdmin(admin.ModelAdmin):
    list_display = ('t_id', 'transaction', 'item', 'quantity', 'price')
    search_fields = ('t_id', 'transaction', 'item', 'quantity', 'price')
    list_filter = ('t_id', 'transaction', 'item', 'quantity', 'price')


admin.site.register(customer, customerAdmin)
admin.site.register(cust_Transaction)
admin.site.register(TransactionItem)
