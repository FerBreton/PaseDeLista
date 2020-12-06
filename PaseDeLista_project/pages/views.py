from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View 
from .models import *
from .forms import *

# Create your views here.

class home(View):
    def get(self, request):
        return render(request, 'index.html', {})

class homeAlumno(View):
    def get(self, request):
        alumnos = Alumno.objects.all()

        context = {'alumnos' : alumnos}
        return render(request, 'alumno.html', context)

class AlumnoAdd(View):
    def get(self, request):
        form = AlumnoForm()
        context = {'form' : form}
        return render(request, 'alumnoup.html', context)
    
    def post(self, request):
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homealu')
        else:
            form = AlumnoForm()
            context = {'form' : form}
            return render(request, 'alumnoup.html', context)

class AlumnoUpdate(View):
    def get(self, request, id):
        alumno = Alumno.objects.get(id=id)
        form = AlumnoForm(instance = alumno)
        context = {'form' : form}
        return render(request, 'alumnoup.html', context)
    
    def post(self, request, id):
        alumno = Alumno.objects.get(id=id)
        form = AlumnoForm(request.POST, instance = alumno)
        if form.is_valid():
            form.save()
            return redirect('homealu')
        else:
            context = {'form' : form}
            return render(request, 'alumnoup.html', context)