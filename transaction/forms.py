from django import forms
from transaction.models import TransactionItem, cust_Transaction, item_Transaction


class item_TransactioForm(forms.ModelForm):
    class Meta:
        model = item_Transaction
        fields = "__all__"


class custTransactionForm(forms.ModelForm):
    class Meta:
        model = cust_Transaction
        fields = "__all__"
        labels = {
            "c_id": "Customer",
            "total_amt": "Total Amount",
            "paid_amt": "Paid Amount",
            "balance": "Balance Amount",
        }
        widgets = {
            "c_id": forms.Select(attrs={"class": "form-control"}),
            "total_amt": forms.TextInput(attrs={"class": "form-control"}),
            "paid_amt": forms.TextInput(attrs={"class": "form-control"}),
            "balance": forms.TextInput(attrs={"class": "form-control"}),
        }


class TransactionItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        transaction = kwargs.pop('transaction', None)
        super().__init__(*args, **kwargs)
        if transaction:
            self.fields['transaction'].initial = transaction

    class Meta:
        model = TransactionItem
        fields = "transaction", "items", "quantity"
        labels = {
            "transaction": "Transaction",
            "items": "Items",
            "quantity": "Quantity",
        }
        widgets = {
            "transaction": forms.HiddenInput(),
            "items": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.TextInput(attrs={"class": "form-control"}),
        }
