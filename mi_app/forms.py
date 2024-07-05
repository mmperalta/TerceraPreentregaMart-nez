from django import forms 
from .models import Cliente

class ClienteForm (forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    project = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254,required=True)

class ProyectoForm (forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    shots = forms.CharField(max_length=50)
    cotizacion = forms.IntegerField(required=True)  
    fechaEntrega = forms.DateField(required=True)
    delivered = forms.BooleanField(required=True)

class PagoForm (forms.Form):
    formaPago= forms.CharField(max_length=50,required=True)
    descuento = forms.IntegerField(required=True)