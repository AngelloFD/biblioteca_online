from django.contrib import admin
from .models import Categoria, Libro, Estado, ReclamoUsuario, Actividad

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Estado)
admin.site.register(ReclamoUsuario)
admin.site.register(Actividad)
