from django.contrib import admin
from inventory.models import item, item_Transaction


class itemAdmin(admin.ModelAdmin):
    list_display = ('i_id', 'name', 'quantity', 'price')
    search_fields = ('name', 'date_added')
    list_filter = ('date_added', 'date_modified')


class item_TransactionAdmin(admin.ModelAdmin):
    list_display = ('t_id', 'i_id', 'type', 'quantity')
    search_fields = ('i_id', 'date_added')
    list_filter = ('date_added', 'type')


admin.site.register(item, itemAdmin)
admin.site.register(item_Transaction, item_TransactionAdmin)
