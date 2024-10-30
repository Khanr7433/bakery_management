from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from inventory.forms import ItemForm
from inventory.models import item


def index(request):
    # getting currnt year for footer
    year = datetime.now().year

    # Listing Items
    items = item.objects.all()

    return render(request, "inventory/index.html", {
        "year": year,                                  "items": items,
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
        # Adding Item
        form = ItemForm()
        return render(request, "inventory/add_item.html", {
            "form": form,
        })


def edit_item(request, i_id):
    item_ = get_object_or_404(item, i_id=i_id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item_)
        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully.")
            return redirect(index)
        else:
            messages.error(request, "Error updating item.")
            return redirect(index)
    else:
        form = ItemForm(instance=item_)
        return render(request, "inventory/edit_item.html", {
                      "form": form,
                      "item": item_,
                      })


def delete_item(request, i_id):
    item_ = get_object_or_404(item, i_id=i_id)

    if request.method == "POST":
        if item_.delete():
            messages.success(request, "Item Deleted successfully.")
            return redirect(index)
        else:
            messages.error(request, "Error Deleting item.")
            return redirect(index)
    else:
        return render(request, "inventory/delete_item.html", {
                      "item": item_,
                      })
