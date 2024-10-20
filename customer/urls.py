from django.urls import path

from customer.views import *

urlpatterns = [
    path("",index,name="index")
]
