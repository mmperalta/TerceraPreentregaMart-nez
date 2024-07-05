from django.contrib import admin

# Register your models here.
from mi_app.models import *

class ClienteAdmin (admin.ModelAdmin):
    list_display = ("nombre", "project", "email")

class ProyectoAdmin (admin.ModelAdmin):
    list_display = ("nombre", "fechaEntrega", "shots","cotizacion","delivered")
    list_filter = ("delivered",)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Pago)