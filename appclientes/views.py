from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        return HttpResponse('<h1>Aula Teste do Carlos</h1>')



# Create your views here.
