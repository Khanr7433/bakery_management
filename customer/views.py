from datetime import datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from customer.models import customer, cust_Transaction

from customer.forms import CustomerForm


def index(request):
    year = datetime.now().year

    # listing Customers
    cust = customer.objects.all()

    return render(request, "customer/index.html", {
        "year": year,
        "cust": cust}
    )


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully.")
            return redirect(index)
        else:
            messages.error(request, "Error adding Customer.")
            return redirect(index)
    else:
        # Adding Customer
        form = CustomerForm()
        return render(request, "customer/add_customer.html", {
            "form": form,
        })


def edit_customer(request, c_id):
    cust = get_object_or_404(customer, c_id=c_id)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=cust)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully.")
            return redirect(index)
        else:
            messages.error(request, "Error updating Customer.")
            return redirect(index)
    else:
        form = CustomerForm(instance=cust)
        return render(request, "customer/edit_customer.html", {
                      "form": form,
                      "cust": cust,
                      })


def delete_customer(request, c_id):
    cust = get_object_or_404(customer, c_id=c_id)

    if request.method == "POST":
        if cust.delete():
            messages.success(request, "Customer Deleted successfully.")
            return redirect(index)
        else:
            messages.error(request, "Error Deleting Customer.")
            return redirect(index)
    else:
        return render(request, "customer/delete_customer.html", {
                      "cust": cust,
                      })


def view_customer(request, c_id):
    cust = get_object_or_404(customer, c_id=c_id)
    transactions = cust_Transaction.objects.filter(c_id=c_id)

    return render(request, "customer/view_customer.html", {
        "cust": cust,
        "transactions": transactions,
    })
