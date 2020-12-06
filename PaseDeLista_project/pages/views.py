from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View 
#from .models import Publication, Autor, Comentario 
#from .forms import PublicationForm

# Create your views here.

class home(View):
    def get(self, request):
        publicaciones = Publication.objects.all()

        #impresion en consola de las publicaciones
        for pub in publicaciones:
            print(pub)

        context = {'publicaciones' : publicaciones}
        return render(request, 'index.html', context)

class PublicationAdd(View):
    def get(self, request):
        form = PublicationForm()
        context = {'form' : form}
        return render(request, 'publication.html', context)
    
    def post(self, request):
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = PublicationForm()
            context = {'form' : form}
            return render(request, 'publication.html', context)

class PublicationUpdate(View):
    def get(self, request, id):
        publicacion = Publication.objects.get(id=id)
        form = PublicationForm(instance = publicacion)
        context = {'form' : form}
        return render(request, 'publication.html', context)
    
    def post(self, request, id):
        publicacion = Publication.objects.get(id=id)
        form = PublicationForm(request.POST, instance = publicacion)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {'form' : form}
            return render(request, 'publication.html', context)