from django.urls import path

from .views import asistenciaView

urlpatterns = [
    path('', asistenciaView, name="asistencia"),
]