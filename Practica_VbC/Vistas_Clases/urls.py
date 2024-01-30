from Vistas_Clases.views import Mivista
from django.urls import path

urlpatterns = [
    path("sobre/", Mivista.as_view())
]
