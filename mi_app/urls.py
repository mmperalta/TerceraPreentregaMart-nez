from django.urls import path, include
from mi_app.views import *

urlpatterns = [
    path('', home, name="home"),
]
