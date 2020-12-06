from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View 
from .models import *
from .forms import AlumnoForm

# Create your views here.

class home(View):
    def get(self, request):
        alumnos = Alumno.objects.all()

        #impresion en consola de los alumnos
        for alu in alumnos:
            print(alu)

        context = {'alumnos' : alumnos}
        return render(request, 'index.html', context)

class AlumnoAdd(View):
    def get(self, request):
        form = AlumnoForm()
        context = {'form' : form}
        return render(request, 'alumno.html', context)
    
    def post(self, request):
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = AlumnoForm()
            context = {'form' : form}
            return render(request, 'alumno.html', context)

class AlumnoUpdate(View):
    def get(self, request, id):
        alumno = Alumno.objects.get(id=id)
        form = AlumnoForm(instance = alumno)
        context = {'form' : form}
        return render(request, 'alumno.html', context)
    
    def post(self, request, id):
        alumno = Alumno.objects.get(id=id)
        form = AlumnoForm(request.POST, instance = alumno)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {'form' : form}
            return render(request, 'alumno.html', context)