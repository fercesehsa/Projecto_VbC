from typing import Any
from django.views.generic import ListView,CreateView,TemplateView
from .models import *
from django.shortcuts import render



def Listar(request):
    usuariolista=Usuarios.objects.all()
    return render(request,"Lusuarios.html",{"usuarios":usuariolista})

class Index(TemplateView):
    template_name="index.html"

class Lusers(ListView):
    model=Usuarios
    template_name="Lusuarios.html"

    def get_queryset(self):

        return Usuarios.objects.all()
    
    def get_context_data(self, **kwargs):
        ctx=super().get_context_data(**kwargs)
        ctx['titulo']='Listar usuarios'
        return ctx


class Ltareas(ListView):
    model=Tareas
    template_name="Ltareas.html"

    def get_queryset(self):

        return Tareas.objects.all()
    
    def get_context_data(self, **kwargs):
        ctx=super().get_context_data(**kwargs)
        ctx['titulo']='Listar Tareas'
        return ctx