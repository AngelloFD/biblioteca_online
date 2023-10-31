from django.db import models

# Create your models here.
class Ejemplares(models.Model):
   id_ejemplar = models.CharField(max_length=100, primary_key=True, unique=True, null=False, blank=False)
   libro = models.ForeignKey('core.Libro', on_delete=models.CASCADE)
   estado = models.ForeignKey('core.Estado', on_delete=models.CASCADE)
   numero_ejemplar = models.IntegerField(null=False, blank=False)
   resumen = models.CharField(max_length=1000, null=False, blank=False)
   compuesto = models.CharField(max_length=20, null=False, blank=False)

   def __str__(self):
      return self.id_ejemplar

class Prestamo(models.Model):
   id_prestamo = models.CharField(max_length=80, primary_key=True, unique=True, null=False, blank=False)
   id_ejemplar = models.ForeignKey(Ejemplares, on_delete=models.CASCADE)
   id_usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
   fecha_iniprestamo = models.DateField(null=True, blank=True)
   fecha_finprestamo = models.DateField(null=True, blank=True)
   fecha_devolucion = models.DateField(null=True, blank=True)

   def __str__(self):
      return self.id_prestamo + "_TO_" + self.id_usuario
