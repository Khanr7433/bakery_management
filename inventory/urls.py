from django.urls import path

from inventory.views import index, add_item

urlpatterns = [
    path("", index, name="index"),
    path("add_item", add_item, name="add_item")
]
