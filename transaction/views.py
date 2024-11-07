from django.shortcuts import redirect, render
from customer.models import cust_Transaction, TransactionItem
from inventory.models import item_Transaction
from customer.forms import custTransactionForm, TransactionItemForm

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


def add_transaction(request):
    # Add Transaction
    if request.method == "POST":
        form1 = custTransactionForm(request.POST)
        form2 = TransactionItemForm(request.POST)
        if form1.is_valid():
            form1.save()
            if form2.is_valid():
                form2.save()
                return redirect("transaction:index")
    else:
        form1 = custTransactionForm()
        form2 = TransactionItemForm()
        return render(request, "transaction/add_transaction.html", {
            "form1": form1,
            "form2": form2,
        })
