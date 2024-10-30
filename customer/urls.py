from django.urls import path
from customer.views import *
from customer.views import add_customer, edit_customer, delete_customer

urlpatterns = [
    path("", index, name="index"),
    path("add_customer", add_customer, name="add_customer"),
    path("edit_customer/<int:c_id>", edit_customer, name="edit_customer"),
    path("delete_customer/<int:c_id>", delete_customer, name="delete_customer"),
]
