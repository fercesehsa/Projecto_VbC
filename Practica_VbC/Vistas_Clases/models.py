from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuarios(AbstractBaseUser):
    usenom=models.CharField(max_length=25)
    appuse=models.CharField(max_length=25)
    apmuse=models.CharField(max_length=25)
    edad=models.IntegerField()
    activo=models.BooleanField(default=True)

class Tareas():
    nomtarea=models.CharField(max_length=25)
    desctarea=models.CharField(max_length=150)
    iniciftarea=models.DateField()
    finftarea=models.DateField()
    usuario_tarea=models.ForeignKey(Usuarios, on_delete=models.CASCADE)

