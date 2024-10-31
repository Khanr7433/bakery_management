from django.contrib import admin
from django.urls import path, include
from bakery_management.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('customer/', include('customer.urls')),

    path('inventory/', include('inventory.urls')),

    path('transaction/', include('transaction.urls')),

    path("__reload__/", include("django_browser_reload.urls")),

    path("", index, name="index"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
