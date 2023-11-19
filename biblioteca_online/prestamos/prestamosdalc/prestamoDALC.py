from usuario.models import Usuario
from prestamos.models import Prestamo
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def DALC_GetPrestamoOfUsuario(usuario:Usuario):
    try:
        prestamo = Prestamo.objects.filter(id_usuario=usuario)
        return prestamo
    except ObjectDoesNotExist:
        raise f"Error en DALC_GetPrestamoOfUsuario -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en DALC_GetPrestamoOfUsuario -> {MultipleObjectsReturned}"