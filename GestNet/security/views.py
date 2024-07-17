from django.shortcuts import render

# Create your views here.
# security/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue dans la gestion de la sécurité.")
