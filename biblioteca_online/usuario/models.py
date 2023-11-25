from django.db import models
from django.contrib.auth.models import User
import requests
from core.models import Actividad
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Usuario(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   dni = models.IntegerField(null=True, unique=True) # Forzar en frontend
   fecha_nacimiento = models.DateField(null=True)
   compuesto = models.CharField(max_length=20, null=True)
   email_verificado = models.BooleanField(default=False)  # Nuevo campo
   email_confirmation_token = models.CharField(max_length=255, blank=True, null=True)  # Nuevo campo
   fecha_actualizacion = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.user.username + "_" + str(self.dni) 

@receiver(post_save, sender=User)
def create_Usuario(sender, instance, created,**kwargs):
    if created:
        Usuario.objects.create(user=instance)

def verificar_correo(email):
    kickbox_api_key = "test_2413259a4f8d4f2fcecdc0aa9bdb6796d865559417f3fd0774a244346bbd0cbc" 
    url = f"https://open.kickbox.com/v1/disposable/{email}"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {kickbox_api_key}",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return not data["disposable"]
    else:
        return False

class InformeUsuario(models.Model):
   id_informe = models.CharField(max_length=100, primary_key=True, unique=True, null=False, blank=False)
   id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
   id_actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
   fecha_creacion = models.DateField(auto_now_add=True, null=False, blank=False)
   
   def __str__(self):
      return self.id_informe + " - " + str(self.id_usuario)
