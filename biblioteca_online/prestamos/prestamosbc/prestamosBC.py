from prestamos.prestamosdalc.prestamoDALC import DALC_GetPrestamoOfUsuario,DALC_GetPrestamoByID
from usuario.models import Usuario
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def BC_GetPrestamoOfUsuario(usuario:Usuario):
    try:
        prestamo = DALC_GetPrestamoOfUsuario(usuario)
        return prestamo
    except ObjectDoesNotExist:
        raise f"Error en BC_GetPrestamoOfUsuario -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en BC_GetPrestamoOfUsuario -> {MultipleObjectsReturned}"
    
def BC_GetPrestamoByID(id):
    try:
        prestamo = DALC_GetPrestamoByID(id)
        return prestamo
    except ObjectDoesNotExist:
        raise f"Error en BC_GetPrestamoByID -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en BC_GetPrestamoByID -> {MultipleObjectsReturned}"