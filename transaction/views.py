from django.shortcuts import get_object_or_404, redirect, render
from customer.models import customer
from transaction.forms import TransactionItemForm, custTransactionForm
from transaction.models import TransactionItem, cust_Transaction, item_Transaction


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


def add_transaction(request, c_id):
    cust = get_object_or_404(customer, c_id=c_id)

    # Create the cust_Transaction object
    transaction = cust_Transaction.objects.create(c_id=cust)

    if request.method == 'POST':
        transItem_form = TransactionItemForm(
            request.POST, transaction=transaction)
        if transItem_form.is_valid():
            transItem_form.save()
            return redirect('index')
    else:
        transItem_form = TransactionItemForm(transaction=transaction)

    return render(request, 'transaction/add_transaction.html', {
        'transItem_form': transItem_form
    })
