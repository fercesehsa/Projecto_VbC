from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,View



class Mivista(View):
    def get(self,request): 
        return HttpResponse("hola mundo desde return")
