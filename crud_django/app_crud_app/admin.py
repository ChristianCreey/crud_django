from django.contrib import admin
from .models import Alumno, Maestro, Materia

# Register your models here.
admin.site.register(Materia)
admin.site.register(Alumno)
admin.site.register(Maestro)
