from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def asistenciaView(request):
    return render(request, 'asistencia.html', {})