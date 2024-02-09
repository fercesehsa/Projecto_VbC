
from django.urls import path,include
from Vistas_Clases.views import *

urlpatterns = [
    path('index/', Index.as_view(), name="index"),
    path('listusers/', Lusers.as_view(), name="listausuarios"),
    path('listtareas/', Ltareas.as_view(), name="listatareas"),
    
]