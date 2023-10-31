from django.contrib import admin
from .models import Ejemplares, Prestamo

# Register your models here.
admin.site.register(Ejemplares)
admin.site.register(Prestamo)