from django.contrib import admin
from inventory.models import item


class itemAdmin(admin.ModelAdmin):
    list_display = ('i_id', 'name', 'quantity', 'price')
    search_fields = ('name', 'date_added')
    list_filter = ('date_added', 'date_modified')


admin.site.register(item, itemAdmin)
