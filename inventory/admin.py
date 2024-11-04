from django.contrib import admin
from inventory.models import item, item_Transaction

# Register your models here.
admin.site.register(item)
admin.site.register(item_Transaction)
