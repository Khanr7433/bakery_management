from django.urls import path

from inventory.views import index, add_item, edit_item, delete_item

urlpatterns = [
    path("", index, name="index"),
    path("add_item", add_item, name="add_item"),
    path("edit_item/<int:i_id>", edit_item, name="edit_item"),
    path("delete_item/<int:i_id>", delete_item, name="delete_item"),
]
