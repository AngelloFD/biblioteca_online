from django.db import models
from prestamos.models import Prestamo

# Create your models here.
class Categoria(models.Model):
   id_categoria = models.CharField(max_length=50, primary_key=True, unique=True, null=False, blank=False)
   nombre = models.CharField(max_length=50, null=False, blank=False)

   def __str__(self):
      return self.nombre

class Libro(models.Model):
   id_libro = models.CharField(max_length=100, primary_key=True, unique=True, null=False, blank=False)
   categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
   title = models.CharField(max_length=100, null=False, blank=False)
   author = models.CharField(max_length=50, null=False, blank=False)
   isbn = models.CharField(max_length=50, null=False, blank=False)
   summary = models.CharField(max_length=4000, null=False, blank=False)
   image = models.URLField(max_length=240, null=True, blank=False)

   def save(self, *args, **kwargs):
        # Genera el ID del libro automáticamente
        if not self.id_libro:
            self.id_libro = f"{self.author[0].capitalize()}{self.isbn}"

        super().save(*args, **kwargs)

   def __str__(self):
      return self.title

class Estado(models.Model):
   id_estado = models.AutoField(primary_key=True, unique=True, null=False, blank=False)
   nombre = models.CharField(max_length=20, null=False, blank=False)

   def __str__(self):
      return str(self.id_estado) +" "+ self.nombre

class ReclamoUsuario(models.Model):
   id_reclamo = models.CharField(max_length=80, primary_key=True, unique=True, null=False, blank=False)
   id_prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
   descripcion = models.CharField(max_length=1000, null=False, blank=False)
   imagen = models.ImageField(upload_to='reclamos/', null=True, blank=False)
   fecha_creacion = models.DateField(auto_now_add=True, null=False, blank=False)

   def __str__(self):
      return self.id_reclamo + "_FROM_" + self.id_usuario

class Actividad(models.Model):
   id_actividad = models.CharField(max_length=50, primary_key=True, unique=True, null=False, blank=False)
   descripcion = models.CharField(max_length=500, null=False, blank=False)

   def __str__(self):
      return self.id_actividad
