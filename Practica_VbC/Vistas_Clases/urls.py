from Vistas_Clases.views import *
from django.urls import path

urlpatterns = [
    path("sobre/", Mivista.as_view(), name='index'),
    path("crearusuario/", Registrarusuario.as_view(), name='Registrar')
]
