from django.shortcuts import render
from customer.models import cust_Transaction, TransactionItem
from inventory.models import item_Transaction

# Create your views here.


def index(request):
    # Transaction of Customer
    cust_Trans = cust_Transaction.objects.all()

    # items of Customer Transaction
    items = TransactionItem.objects.all()

    # transaction of Inventory
    item_Trans = item_Transaction.objects.all()

    return render(request, "transaction/index.html", {
        "cust": cust_Trans,
        "items": items,
        "item_Trans": item_Trans,
    })
