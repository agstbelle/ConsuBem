from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index (request):
    return render (request, 'index.html')

def cadastro (request):
    return render (request, 'cadastro.html')

def login (request):
    return render (request, 'login.html')

