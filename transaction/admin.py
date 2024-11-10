from django.contrib import admin
from transaction.models import TransactionItem, cust_Transaction, item_Transaction


class item_TransactionAdmin(admin.ModelAdmin):
    list_display = ('t_id', 'i_id', 'type', 'quantity')
    search_fields = ('i_id', 'date_added')
    list_filter = ('date_added', 'type')


class cust_TransactionAdmin(admin.ModelAdmin):
    list_display = ('t_id', 'c_id', 'total_amt', 'paid_amt', 'balance')
    search_fields = ('t_id', 'c_id', 'total_amt', 'paid_amt', 'balance')
    list_filter = ('t_id', 'c_id', 'total_amt', 'paid_amt', 'balance')


class TransactionItemAdmin(admin.ModelAdmin):
    list_display = ('t_id', 'transaction', 'items', 'quantity', 'price')
    search_fields = ('t_id', 'transaction', 'items', 'quantity', 'price')
    list_filter = ('t_id', 'transaction', 'items', 'quantity', 'price')


admin.site.register(item_Transaction, item_TransactionAdmin)
admin.site.register(cust_Transaction, cust_TransactionAdmin)
admin.site.register(TransactionItem, TransactionItemAdmin)
