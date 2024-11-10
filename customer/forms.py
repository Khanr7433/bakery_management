from django import forms
from customer.models import customer


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
