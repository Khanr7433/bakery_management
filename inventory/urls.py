from django.urls import path

from inventory.views import index

urlpatterns = [
    path("",index,name="index")
]
