from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Clase)
admin.site.register(Materia)
admin.site.register(Profesor)
admin.site.register(Asistencia)