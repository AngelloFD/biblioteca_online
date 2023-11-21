# bibliotecario/urls.py

from django.urls import path
from . import views

app_name = "bibliotecario"

urlpatterns = [
    path('panel_bibliotecario', views.panel_bibliotecario, name='panel_bibliotecario'),
    path('libros', views.libros, name='libros'),
    path('prestamos', views.prestamos, name='prestamos'),
    path('dashboardBooker/', views.dashboard_booker, name='dashboardBooker'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('registrar_ejemplar/', views.registrar_ejemplar, name='registrar_ejemplar'),
    path('registrar_prestamo/', views.registrar_prestamo, name='registrar_prestamo'),
    path('visualizar_prestamos/', views.visualizar_prestamos, name='visualizar_prestamos'),
    path('visualizar_prestamos/modificar/<str:id_prestamo>/', views.modificar_estado_prestamo, name='modificar_estado_prestamo'),
]