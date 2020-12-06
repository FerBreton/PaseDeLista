from django import forms
from .models import *

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre']

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['grupo', 'fecha_clase', 'materia']