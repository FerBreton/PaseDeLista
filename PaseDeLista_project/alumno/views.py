from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def alumnoView(request):
    return render(request, 'alumno.html', {})