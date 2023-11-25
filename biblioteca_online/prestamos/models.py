from django.db import models

# Create your models here.
class Ejemplares(models.Model):
   id_ejemplar = models.CharField(max_length=100, primary_key=True, unique=True, null=False, blank=False)
   libro = models.ForeignKey('core.Libro', on_delete=models.CASCADE)
   estado = models.ForeignKey('core.Estado', on_delete=models.CASCADE)
   resumen = models.CharField(max_length=1000, null=False, blank=False)
   compuesto = models.CharField(max_length=20, null=False, blank=False)

   def __str__(self):
      return self.id_ejemplar

class Prestamo(models.Model):
   id_prestamo = models.CharField(max_length=80, primary_key=True, unique=True, null=False, blank=False)
   id_ejemplares = models.CharField(max_length=4000,null=False, blank=False, default="vacio")
   id_usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
   prestado_estado = models.ForeignKey('prestamos.PrestamoEstado', on_delete=models.CASCADE, default="En espera")
   fecha_iniprestamo = models.DateField(null=True, blank=True)
   fecha_finprestamo = models.DateField(null=True, blank=True)
   fecha_devolucion = models.DateField(null=True, blank=True)

   def __str__(self):
      return self.id_prestamo + "_TO_" + str(self.id_usuario)

class PrestamoEstado(models.Model):
   id_prestado = models.CharField(max_length=80, primary_key=True, unique=True, null=False, blank=False)
   prestado = models.CharField(max_length=80,null=False, blank=False, default="invalido")
   def __str__(self):
      return self.prestado