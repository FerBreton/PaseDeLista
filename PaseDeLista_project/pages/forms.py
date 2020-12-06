from django import forms
from .models import *

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre']

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'periodo', 'year']

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['grupo', 'fecha_clase', 'materia']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'materia']

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['clase', 'alumno', 'fecha_asistencia']