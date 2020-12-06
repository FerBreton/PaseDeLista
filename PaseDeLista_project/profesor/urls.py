from django.urls import path

from .views import profesorView

urlpatterns = [
    path('', profesorView, name="profesor"),
]