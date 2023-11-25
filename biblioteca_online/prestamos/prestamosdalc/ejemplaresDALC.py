from prestamos.models import Prestamo
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def DALC_GetEjemplarbyID(id):
    try:
        ejemplar = Prestamo.objects.filter(id_usuario=id)
        return ejemplar
    except ObjectDoesNotExist:
        raise f"Error en DALC_GetEjemplarbyID -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en DALC_GetEjemplarbyID -> {MultipleObjectsReturned}"
    


    
