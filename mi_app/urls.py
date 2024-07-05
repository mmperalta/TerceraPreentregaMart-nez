from django.urls import path, include
from mi_app.views import *

urlpatterns = [
    path('', home, name="home"),
    path('pago/', pago, name="pago"),
    path('cliente/', cliente, name="cliente"),
    path('proyecto/', proyecto, name="proyecto"),
]
