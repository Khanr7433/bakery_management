from django.conf import settings
from django.urls import path
from customer.views import index, add_customer, edit_customer, delete_customer, view_customer
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("add_customer", add_customer, name="add_customer"),
    path("edit_customer/<int:c_id>", edit_customer, name="edit_customer"),
    path("delete_customer/<int:c_id>", delete_customer, name="delete_customer"),
    path("view_customer/<int:c_id>", view_customer, name="view_customer"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
