# security/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='security_index'),
    # Ajoutez d'autres chemins ici
]
