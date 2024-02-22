from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.views.generic import *
from .models import *
from django.shortcuts import render,redirect



def Listar(request):
    usuariolista=Usuarios.objects.all()
    return render(request,"Lusuarios.html",{"usuarios":usuariolista})

class Index(TemplateView):
    template_name="index.html"

class Lusers(ListView):
    model=Usuarios
    template_name="Lusuarios.html"

    def get_queryset(self):

        return Usuarios.objects.filter(activo=True)
    
    def get_context_data(self, **kwargs):
        ctx=super().get_context_data(**kwargs)
        ctx['titulo']='Listar usuarios'
        return ctx


class Ltareas(ListView):
    model=Tareas
    template_name="Ltareas.html"

    def get_queryset(self):
        
        return Tareas.objects.filter(status=True)
        

    
    def get_context_data(self, **kwargs):
        ctx=super().get_context_data(**kwargs)
        ctx['titulo']='Listar Tareas'
        return ctx


class Musuarios(UpdateView):
    model=Usuarios
    template_name='Musuario.html'
    fields=['usenom','appuse','apmuse','edad','activo']
    success_url=reverse_lazy('listausuarios')

class Mtareas(UpdateView):
    model=Tareas
    template_name='Mtareas.html'
    fields=['nomtarea','desctarea','iniciftarea','finftarea','usuario_tarea']
    success_url=reverse_lazy('listatareas')

class Crearusuarios(CreateView):
    model=Usuarios
    template_name='Cusuarios.html'
    fields=['usenom','appuse','apmuse','edad','activo']
    success_url=reverse_lazy('listausuarios')

class Creartareas(CreateView):
    model=Tareas
    template_name='Ctareas.html'
    fields=['nomtarea','desctarea','iniciftarea','finftarea','usuario_tarea']
    success_url=reverse_lazy('creatareas')

class Deletetarea(DeleteView):
    model=Tareas

    def post(self,request,pk, *args, **kwargs):
        object=Tareas.objects.get(id=pk)
        object.status=False
        object.save()
        return redirect('listatareas')

    
  
    

    
