from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from mi_app.models import *
from .forms import *

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

#Formularios

def clienteForm (request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_project = miForm.cleaned_data.get("project")
            cliente_mail = miForm.cleaned_data.get("email")
            cliente = Cliente(nombre=cliente_nombre, project=cliente_project, email=cliente_mail)
            cliente.save()
            contexto = {"cliente": Cliente.objects.all()}
            return render(request, 'mi_app/cliente.html', contexto)
    else:
        miForm = ClienteForm()

    return render(request, "mi_app/clienteForm.html", {"form":miForm})

def proyectoForm (request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            proyecto_nombre = miForm.cleaned_data.get("nombre")
            proyecto_shots = miForm.cleaned_data.get("shots")
            proyecto_cotizacion = miForm.cleaned_data.get("cotizacion")
            proyecto_fechaEntrega = miForm.cleaned_data.get("fechaEntrega")
            proyecto_delivered= miForm.cleaned_data.get("delivered")
            proyecto = Proyecto(nombre=proyecto_nombre, shots=proyecto_shots, cotizacion=proyecto_cotizacion, fechaEntrega = proyecto_fechaEntrega, delivered = proyecto_delivered)
            proyecto.save()
            contexto = {"proyecto": Proyecto.objects.all()}
            return render(request, 'mi_app/proyecto.html', contexto)
    else:
        miForm = ProyectoForm()

    return render(request, "mi_app/proyectoForm.html", {"form":miForm})

def pagoForm (request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            pago_formaPago = miForm.cleaned_data.get("formaPago")
            pago_descuento = miForm.cleaned_data.get("descuento")
            pago = Pago(formaPago=pago_formaPago, descuento=pago_descuento)
            pago.save()
            contexto = {"pago": Pago.objects.all()}
            return render(request, 'mi_app/pago.html', contexto)
    else:
        miForm = PagoForm()

    return render(request, "mi_app/pagoForm.html", {"form":miForm})

#Buscar clientes

def buscarCliente (request):
    return render (request, "mi_app/buscarCliente.html")

def encontrarCliente (request):
    if request.GET["buscar"]:
        patron= request.GET["buscar"]
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {'cliente': clientes}
    else:
        contexto = {'cliente': Cliente.objects.all()}
    
    return render(request, 'mi_app/cliente.html', contexto)