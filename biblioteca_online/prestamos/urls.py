from django.urls import path
from . import views

app_name = "prestamos"

urlpatterns = [
    path(
        "detalle_prestamo/<str:id_prestamo>/",
        views.detalle_prestamo,
        name="detalle_prestamo",
    ),
]
