from django import forms
from inventory.models import item


class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = "__all__"
