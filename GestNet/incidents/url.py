# incidents/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='incidents_index'),
    # Ajoutez d'autres chemins ici
]
