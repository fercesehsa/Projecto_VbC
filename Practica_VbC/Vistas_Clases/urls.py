
from django.urls import path,include
from Vistas_Clases.views import *

urlpatterns = [
    path('', Lusers.as_view(), name="listausuarios"),
    
]