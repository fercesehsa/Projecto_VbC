
from django.urls import path,include
from Vistas_Clases.views import *

urlpatterns = [
    path('index/', Index.as_view(), name="index"),
    path('listusers/', Lusers.as_view(), name="listausuarios"),
    path('listtareas/', Ltareas.as_view(), name="listatareas"),
    path('editarusuarios/<int:pk>', Musuarios.as_view(), name="modificarusuarios"),
    path('editartareas/<int:pk>', Mtareas.as_view(), name="modificartareas"),
    path('crearusuario/', Crearusuarios.as_view(), name="crearusuario"),
    
]