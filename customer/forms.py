from django import forms

from customer.models import customer, cust_Transaction, TransactionItem


class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = "__all__"
        labels = {
            "name": "Name",
            "phone": "Phone",
            "address": "Address",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
        }


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
    class Meta:
        model = TransactionItem
        fields = "__all__"
        labels = {
            "transaction": "Transaction",
            "items": "Items",
            "quantity": "Quantity",
            "Price": "Price",
        }
        widgets = {
            "transaction": forms.Select(attrs={"class": "form-control"}),
            "items": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.TextInput(attrs={"class": "form-control"}),
            "Price": forms.TextInput(attrs={"class": "form-control"}),
        }
