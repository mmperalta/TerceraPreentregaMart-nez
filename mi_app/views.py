from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from mi_app.models import *

import datetime, random

def clienteNuevo (request):
    nombre = 'Prime Video'
    nombre_proyecto = 'Red One'
    mail = 'john@amazonstudios.com'
    cliente = Cliente(nombre=nombre, project=nombre_proyecto, email=mail)
    cliente.save()

    #___________Creando objeto proyecto 

    nombrep = cliente.get_cliente_project()
    shots = random.randint(100,400)
    cotizacion = random.randint(6000,400000)
    #fechaEntrega = models.DateField()
    delivered = random.choice([True, False])
    project = Proyecto( nombrep = nombre, shots=shots, cotizacion=cotizacion, delivered=delivered)
    project.save()


def formaPago (request):
    formaPago= random.choice(['cash', 'credit'])
    descuento = random.randint(10,65)
    payment = Pago(formaPago=formaPago, descuento=descuento)
    payment.save()


def home(request):
    return render(request, 'mi_app/index.html')

# Create your views here.
