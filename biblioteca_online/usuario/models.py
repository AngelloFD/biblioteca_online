from django.db import models
from core.models import Actividad

# Create your models here.
class Estado(models.Model):
   id_estado = models.AutoField(primary_key=True, unique=True, null=False, blank=False)
   nombre = models.CharField(max_length=20, null=False, blank=False)

   def __str__(self):
      return self.id_estado + self.nombre

class Usuario(models.Model):
   id_usuario = models.CharField(max_length=20, primary_key=True, unique=True, null=False, blank=False)
   estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
   nombre = models.CharField(max_length=50, null=False, blank=False)
   apellido = models.CharField(max_length=100, null=False, blank=False)
   username = models.CharField(max_length=100, null=False, blank=False, unique=True)
   email = models.EmailField(null=False, blank=False, unique=True)
   password = models.CharField(max_length=256, null=False, blank=False)
   fecha_nacimiento = models.DateField()
   compuesto = models.CharField(max_length=20, null=False, blank=False)
   fecha_registro = models.DateTimeField(auto_now_add=True, null=False, blank=False)
   fecha_actualizacion = models.DateTimeField(auto_now=True, null=False, blank=False)

   def __str__(self):
      return self.nombre + " " + self.apellido

class InformeUsuario(models.Model):
   id_informe = models.CharField(max_length=100, primary_key=True, unique=True, null=False, blank=False)
   id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
   id_actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
   fecha_creacion = models.DateField(auto_now_add=True, null=False, blank=False)
   
   def __str__(self):
      return self.id_informe + " " + self.id_usuario
