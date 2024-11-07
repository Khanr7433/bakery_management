from django import forms
from inventory.models import item, item_Transaction


class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = "__all__"


class item_Transactio(forms.ModelForm):
    class Meta:
        model = item_Transaction
        fields = "__all__"
