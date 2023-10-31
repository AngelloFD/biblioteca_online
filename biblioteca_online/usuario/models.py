from django.db import models
from django.contrib.auth.models import User
from core.models import Actividad
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Usuario(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   dni = models.IntegerField(null=True, unique=True) # Forzar en frontend
   fecha_nacimiento = models.DateField(null=True)
   compuesto = models.CharField(max_length=20, null=True)
   fecha_actualizacion = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.user.username + "_" + str(self.dni) 

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
