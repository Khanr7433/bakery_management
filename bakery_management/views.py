from django.shortcuts import render
from datetime import datetime


def index(request):
    year = datetime.now().year
    return render(request, "home/index.html", {"year": year})
