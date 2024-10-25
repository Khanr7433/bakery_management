from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    year = datetime.now().year
    return render(request, "inventory/index.html",{"year":year})

def add_item(request):
    pass

def edit_item(request):
    pass

def delete_item(request):
    pass

def item_list(request):
    pass



