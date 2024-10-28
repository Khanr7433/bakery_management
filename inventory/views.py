from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from inventory.forms import ItemForm
from inventory.models import item


def index(request):
    # getting currnt year for footer
    year = datetime.now().year

    # Listing Items
    items = item.objects.all()

    # Adding Item
    form = ItemForm()

    return render(request, "inventory/index.html", {
        "year": year,                                  "items": items,
        "form": form,
    })


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item added successfully.")
            return redirect(index)
        else:
            messages.error(request, "Error adding item.")
            return redirect(index)
    else:
        render(request, "inventory/index.html")


def edit_item(request):
    pass


def delete_item(request):
    pass
