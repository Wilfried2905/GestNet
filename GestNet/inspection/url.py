# inspection/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inspection_index'),
    # Ajoutez d'autres chemins ici
]
