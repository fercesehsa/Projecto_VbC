from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Usuario_form(UserCreationForm):
    usenom=forms.CharField(max_length=25)
    appuse=forms.CharField(max_length=25)
    apmuse=forms.CharField(max_length=25)
    edad=forms.IntegerField()

    class Meta:
        model=Usuarios
        fields=['usenom','appuse','apmuse','edad']

