from prestamos.prestamosdalc.prestamoDALC import DALC_GetPrestamoOfUsuario
from usuario.models import Usuario
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def BC_GetPrestamoOfUsuario(usuario:Usuario):
    try:
        prestamo = DALC_GetPrestamoOfUsuario(usuario)
        return prestamo
    except ObjectDoesNotExist:
        raise f"Error en DALC_GetPrestamoOfUsuario -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en DALC_GetPrestamoOfUsuario -> {MultipleObjectsReturned}"