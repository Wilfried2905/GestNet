from django.shortcuts import render

# Create your views here.
# inspection/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue dans l'inspection et validation.")
