from django.contrib import admin
from .models import Ejemplares, Prestamo, PrestamoEstado

# Register your models here.
admin.site.register(Ejemplares)
admin.site.register(Prestamo)
admin.site.register(PrestamoEstado)