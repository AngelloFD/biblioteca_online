from prestamos.models import Prestamo
from prestamos.prestamosdalc.prestamoDALC import DALC_GetPrestamoOfUsuario,DALC_GetPrestamoByID, DALC_crearPrestamo
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
    
def BC_crearPrestamo(id_prestamo, id_ejemplares, id_usuario, prestamo_estado, fecha_iniprestamo, fecha_finprestamo, fecha_devolucion):
    try:
        prestamo = Prestamo(id_prestamo, id_ejemplares, id_usuario, prestamo_estado, fecha_iniprestamo, fecha_finprestamo, fecha_devolucion)
        return DALC_crearPrestamo(prestamo)
    except ObjectDoesNotExist:
        raise f"Error en DALC_GetPrestamoByID -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en DALC_GetPrestamoByID -> {MultipleObjectsReturned}"