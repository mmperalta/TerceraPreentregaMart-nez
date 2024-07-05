from django.urls import path, include
from mi_app.views import *

urlpatterns = [
    path('', home, name="home"),
    path('pago/', pago, name="pago"),
    path('cliente/', cliente, name="cliente"),
    path('proyecto/', proyecto, name="proyecto"),
    path('sobremi/', sobremi, name="sobremi"),

    #Formularios
    path('clienteForm/', clienteForm, name="clienteForm"),
    path('proyectoForm/', proyectoForm, name="proyectoForm"),
    path('pagoForm/', pagoForm, name="pagoForm"),

    #Buscar
    path('buscarCliente/', buscarCliente, name="buscarCliente"),
    path('encontrarCliente/', encontrarCliente, name="encontrarCliente"),
]
