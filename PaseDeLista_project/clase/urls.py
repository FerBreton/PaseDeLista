from django.urls import path

from .views import claseView

urlpatterns = [
    path('', claseView, name="clase"),
]