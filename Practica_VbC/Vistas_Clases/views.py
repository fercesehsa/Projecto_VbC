from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView,CreateView
from .models import *
from django.shortcuts import render



def Listar(request):
    usuariolista=Usuarios.objects.all()
    return render(request,"Regis_usuario.html",{"usuarios":usuariolista})

class Lusers(ListView):
    model=Usuarios
    template_name="Regis_usuario.html"

    def get_queryset(self):

        return Usuarios.objects.all()
    
    def get_context_data(self, **kwargs):
        ctx=super().get_context_data(**kwargs)
        ctx['titulo']='Listar usuarios'
        return ctx


