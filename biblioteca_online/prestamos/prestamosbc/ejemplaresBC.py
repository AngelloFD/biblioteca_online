from prestamos.prestamosdalc.ejemplaresDALC import DALC_GetEjemplarbyID
from usuario.models import Usuario
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def BC_GetEjemplarbyID(id):
    try:
        ejemplar = DALC_GetEjemplarbyID(id)
        return ejemplar
    except ObjectDoesNotExist:
        raise f"Error en BC_GetEjemplarbyID -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en BC_GetEjemplarbyID -> {MultipleObjectsReturned}"
    