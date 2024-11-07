from django.urls import path
from transaction.views import index, add_transaction
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", index, name="index"),
    path("add_transaction/", add_transaction, name="add_transaction"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
