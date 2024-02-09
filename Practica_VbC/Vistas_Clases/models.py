from django.db import models


class Usuarios(models.Model):
    usenom=models.CharField(max_length=25)
    appuse=models.CharField(max_length=25)
    apmuse=models.CharField(max_length=25)
    edad=models.IntegerField()
    activo=models.BooleanField(default=True)

    def __str__(self):
        datos="{0}"
        return datos.format(self.usenom)

class Tareas(models.Model):
    nomtarea=models.CharField(max_length=25)
    desctarea=models.CharField(max_length=150)
    iniciftarea=models.DateField()
    finftarea=models.DateField()
    usuario_tarea=models.ForeignKey(Usuarios, on_delete=models.CASCADE)

