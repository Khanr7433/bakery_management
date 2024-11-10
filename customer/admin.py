from django.contrib import admin
from customer.models import customer


class customerAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'name', 'address', 'phone')
    search_fields = ('c_id', 'name', 'address', 'phone')
    list_filter = ('c_id', 'name', 'address', 'phone')


admin.site.register(customer, customerAdmin)
