from django.db import models
from django.contrib.auth.models import User
from core.models import Actividad
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Usuario(models.Model):
   # Todo con el objetivo de utilizar el usuario default para el login y registro de usuarios
   #id_usuario = models.CharField(max_length=20, primary_key=True, unique=True, null=False, blank=False)
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   dni = models.IntegerField(null=True, unique=True) # Forzar en frontend
   #estado = models.ForeignKey(Estado, on_delete=models.CASCADE) reemplazado por is_superuser / is_staff
   #nombre = models.CharField(max_length=50, null=False, blank=False) reemplazado por first_name
   #apellido = models.CharField(max_length=100, null=False, blank=False) reemplazado por last_name
   #username = models.CharField(max_length=100, null=False, blank=False, unique=True) reemplazado por username
   #email = models.EmailField(null=False, blank=False, unique=True) reemplazado por email
   #password = models.CharField(max_length=256, null=False, blank=False) reemplazado por password
   fecha_nacimiento = models.DateField(null=True)
   compuesto = models.CharField(max_length=20, null=True) # TODO: Q chcha trataba?
   #fecha_registro = models.DateTimeField(auto_now_add=True, null=False, blank=False) reemplazado por date_joined
   fecha_actualizacion = models.DateTimeField(auto_now=True, null=False, blank=False)

   def __str__(self):
      return self.nombre + " " + self.apellido

@receiver(post_save, sender=User)
def create_Usuario(sender, instance, created,**kwargs):
    if created:
        Usuario.objects.create(user=instance)

class InformeUsuario(models.Model):
   id_informe = models.CharField(max_length=100, primary_key=True, unique=True, null=False, blank=False)
   id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
   id_actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
   fecha_creacion = models.DateField(auto_now_add=True, null=False, blank=False)
   
   def __str__(self):
      return self.id_informe + " " + self.id_usuario
