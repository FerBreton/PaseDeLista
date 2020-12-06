from django.urls import path

from .views import alumnoView

urlpatterns = [
    path('', alumnoView, name="alumno"),
]