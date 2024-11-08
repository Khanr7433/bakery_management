from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class user_login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class user_register(UserCreationForm):
    firstname = forms.CharField()
    lastname = forms.CharField()

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'username',
                  'email', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
