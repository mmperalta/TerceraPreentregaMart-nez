from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from mi_app.models import *

import datetime, random

# Create your views here.


def home(request):
    return render(request, 'mi_app/index.html')

def sobremi(request):
    return render(request, 'mi_app/sobremi.html')

def pago(request):
    contexto = {"pago":Pago.objects.all()}
    return render(request, 'mi_app/pago.html', contexto)

def cliente(request):
    contexto = {"cliente":Cliente.objects.all()}
    return render(request, 'mi_app/cliente.html', contexto)

def proyecto(request):
    contexto = {"proyecto": Proyecto.objects.all()}
    return render(request, 'mi_app/proyecto.html', contexto)


