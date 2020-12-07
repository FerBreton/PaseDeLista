from django.urls import path

from .views import *

urlpatterns = [
    path('', home.as_view(), name = "home"),
    path('alumno/home', homeAlumno.as_view(), name = "homealu"),
    path('alumno/add', AlumnoAdd.as_view(), name = "alu_add"),
    path('alumno/<int:id>/', AlumnoUpdate.as_view(), name = "alu_update"),
    path('profesor/home', homeProfesor.as_view(), name = "homepro"),
    path('profesor/add', ProfesorAdd.as_view(), name = "pro_add"),
    path('profesor/<int:id>/', ProfesorUpdate.as_view(), name = "pro_update"),
    path('materia/home', homeMateria.as_view(), name = "homemat"),
    path('materia/add', MateriaAdd.as_view(), name = "mat_add"),
    path('materia/<int:id>/', MateriaUpdate.as_view(), name = "mat_update")
]