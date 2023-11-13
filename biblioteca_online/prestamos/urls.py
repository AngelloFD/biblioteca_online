from django.urls import path
from . import views

app_name = "prestamos"

urlpatterns = [
   path('detalle', views.prestamo_frontend, name="frontendprestamo"), # main/prestamo/detalle
]