from django.db import models

# Create your models here.
class Cliente (models.Model):
    nombre=  models.CharField(max_length=50)
    project= models.CharField(max_length=200)
    email = models.EmailField()

    def get_cliente_project(self):
        return self.project

class Proyecto (models.Model):
    nombre = models.CharField(max_length=50)
    shots = models.IntegerField()
    cotizacion = models.IntegerField()
    fechaEntrega = models.DateField()
    delivered = models.BooleanField()

class Pago (models.Model):
    formaPago= models.CharField(max_length=50)
    descuento = models.IntegerField()

