from django.shortcuts import render
from django.http import HttpResponse

from .models import Categoria

def home(request):
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'categorias': categorias})