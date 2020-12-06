from django.urls import path

from .views import materiaView

urlpatterns = [
    path('', materiaView, name="materia"),
]