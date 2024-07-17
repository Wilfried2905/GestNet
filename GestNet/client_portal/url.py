# client_portal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='client_portal_index'),
    # Ajoutez d'autres chemins ici
]
