from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,View,CreateView,ListView
from .forms import Usuario_form
from django.urls import reverse_lazy



class Mivista(View):
    def get(self,request): 
        return HttpResponse("hola mundo desde return")
    
class Registrarusuario(CreateView):
    def get(self,request):
    ctx={
        'titulo':'Probando'
    }
    return render(request,"Regis_usuario.html",ctx)
