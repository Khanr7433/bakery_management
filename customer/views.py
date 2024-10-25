from datetime import datetime
from django.shortcuts import render


def index(request):
    year = datetime.now().year
    return render(request, "customer/index.html",{"year":year})
