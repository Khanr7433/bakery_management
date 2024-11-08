from django.contrib import messages
from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib import auth
from bakery_management.forms import user_login, user_register


def index(request):
    year = datetime.now().year
    return render(request, "home/index.html", {"year": year})


def login(request):
    if request.method == "POST":
        form = user_login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You are now logged in")
                return redirect('index')
            else:
                messages.error(request, "Invalid login")
                return redirect('login')

    login_form = user_login()
    return render(request, "home/login.html", {
        "form": login_form
    })


def register(request):
    if request.method == "POST":
        form = user_register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            messages.success(request, "You are now registered")
            return redirect('index')
        else:
            messages.error(request, "Invalid registration")
            return redirect('register')

    form = user_register()
    return render(request, "home/register.html", {
        "form": form
    })


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
    return redirect('index')
