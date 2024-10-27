from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    # getting currnt year for footer
    year = datetime.now().year

    # Listing Items
    items = item.objects.all()

    return render(request, "inventory/index.html", {
        "year":year,                                  "items": items,
    })


def add_item(request):

    pass


def edit_item(request):
    pass


def delete_item(request):
    pass


def item_list(request):

    return render()
