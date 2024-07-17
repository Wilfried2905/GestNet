# client_portal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Ajoutez d'autres chemins ici
]

