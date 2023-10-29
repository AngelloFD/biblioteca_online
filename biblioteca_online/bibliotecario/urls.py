# bibliotecario/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('panel_bibliotecario', views.panel_bibliotecario, name='panel_bibliotecario'),
    path('libros', views.libros, name='libros'),
    path('prestamos', views.prestamos, name='prestamos'),
]