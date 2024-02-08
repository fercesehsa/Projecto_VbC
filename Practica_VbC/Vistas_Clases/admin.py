from django.contrib import admin
from .models import *

@admin.register(Usuarios)
class Useradmin(admin.ModelAdmin):
    list_display=('id','usenom')