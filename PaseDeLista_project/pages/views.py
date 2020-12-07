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

class homeProfesor(View):
    def get(self, request):
        profesores = Profesor.objects.all()

        context = {'profesores' : profesores}
        return render(request, 'profesor.html', context)

class ProfesorAdd(View):
    def get(self, request):
        form = ProfesorForm()
        context = {'form' : form}
        return render(request, 'profesorup.html', context)
    
    def post(self, request):
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepro')
        else:
            form = ProfesorForm()
            context = {'form' : form}
            return render(request, 'profesorup.html', context)

class ProfesorUpdate(View):
    def get(self, request, id):
        profesor = Profesor.objects.get(id=id)
        form = ProfesorForm(instance = profesor)
        context = {'form' : form}
        return render(request, 'profesorup.html', context)
    
    def post(self, request, id):
        profesor = Profesor.objects.get(id=id)
        form = ProfesorForm(request.POST, instance = profesor)
        if form.is_valid():
            form.save()
            return redirect('homepro')
        else:
            context = {'form' : form}
            return render(request, 'profesorup.html', context)

class homeMateria(View):
    def get(self, request):
        materias = Materia.objects.all()

        context = {'materias' : materias}
        return render(request, 'materia.html', context)

class MateriaAdd(View):
    def get(self, request):
        form = MateriaForm()
        context = {'form' : form}
        return render(request, 'materiaup.html', context)
    
    def post(self, request):
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homemat')
        else:
            form = MateriaForm()
            context = {'form' : form}
            return render(request, 'materiaup.html', context)

class MateriaUpdate(View):
    def get(self, request, id):
        materia = Materia.objects.get(id=id)
        form = MateriaForm(instance = materia)
        context = {'form' : form}
        return render(request, 'materiaup.html', context)
    
    def post(self, request, id):
        materia = Materia.objects.get(id=id)
        form = MateriaForm(request.POST, instance = materia)
        if form.is_valid():
            form.save()
            return redirect('homemat')
        else:
            context = {'form' : form}
            return render(request, 'materiaup.html', context)

class homeClase(View):
    def get(self, request):
        clases = Clase.objects.all()

        context = {'clases' : clases}
        return render(request, 'clase.html', context)

class ClaseAdd(View):
    def get(self, request):
        form = ClaseForm()
        context = {'form' : form}
        return render(request, 'claseup.html', context)
    
    def post(self, request):
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homecla')
        else:
            form = ClaseForm()
            context = {'form' : form}
            return render(request, 'claseup.html', context)

class ClaseUpdate(View):
    def get(self, request, id):
        clase = Clase.objects.get(id=id)
        form = ClaseForm(instance = clase)
        context = {'form' : form}
        return render(request, 'claseup.html', context)
    
    def post(self, request, id):
        clase = Clase.objects.get(id=id)
        form = ClaseForm(request.POST, instance = clase)
        if form.is_valid():
            form.save()
            return redirect('homecla')
        else:
            context = {'form' : form}
            return render(request, 'claseup.html', context)

class homeAsistencia(View):
    def get(self, request):
        asistencias = Asistencia.objects.all()

        context = {'asistencias' : asistencias}
        return render(request, 'asistencia.html', context)

class AsistenciaAdd(View):
    def get(self, request):
        form = AsistenciaForm()
        context = {'form' : form}
        return render(request, 'asistenciaup.html', context)
    
    def post(self, request):
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeasi')
        else:
            form = AsistenciaForm()
            context = {'form' : form}
            return render(request, 'asistenciaup.html', context)

class AsistenciaUpdate(View):
    def get(self, request, id):
        asistencia = Asistencia.objects.get(id=id)
        form = AsistenciaForm(instance = asistencia)
        context = {'form' : form}
        return render(request, 'asistenciaup.html', context)
    
    def post(self, request, id):
        asistencia = Asistencia.objects.get(id=id)
        form = AsistenciaForm(request.POST, instance = asistencia)
        if form.is_valid():
            form.save()
            return redirect('homeasi')
        else:
            context = {'form' : form}
            return render(request, 'asistenciaup.html', context)