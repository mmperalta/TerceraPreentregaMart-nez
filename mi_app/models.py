from django.db import models

# Create your models here.
class Cliente (models.Model):
    nombre=  models.CharField(max_length=50)
    project= models.CharField(max_length=200)
    email = models.EmailField()

    def get_cliente_project(self):
        return self.project
    
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta: 
        ordering = ["nombre"]

class Proyecto (models.Model):
    nombre = models.CharField(max_length=50)
    shots = models.IntegerField()
    cotizacion = models.IntegerField()
    fechaEntrega = models.DateField()
    delivered = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta: 
        ordering = ["-fechaEntrega"]


class Pago (models.Model):
    formaPago= models.CharField(max_length=50)
    descuento = models.IntegerField()

    def __str__(self):
        return f"{self.formaPago}"


