from django.contrib import admin
from usuario.models import Usuario, InformeUsuario
from .models import Libro, Categoria, Ejemplares, Prestamo, ReclamoUsuario, Actividad

# Register your models here.
admin.site.register(Usuario)
admin.site.register(InformeUsuario)
admin.site.register(Libro)
admin.site.register(Categoria)
admin.site.register(Ejemplares)
admin.site.register(Prestamo)
admin.site.register(ReclamoUsuario)
admin.site.register(Actividad)
