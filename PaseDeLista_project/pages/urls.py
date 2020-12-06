from django.urls import path

from .views import *

urlpatterns = [
    path('', home.as_view(), name = "home"),
    path('alumno/home', homeAlumno.as_view(), name = "homealu"),
    path('alumno/add', AlumnoAdd.as_view(), name = "alu_add"),
    path('alumno/<int:id>/', AlumnoUpdate.as_view(), name = "alu_update")
]