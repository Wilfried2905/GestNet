# execution/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue dans l'exécution des tâches.")

