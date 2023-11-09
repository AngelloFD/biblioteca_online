from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from core.coredalc.librodalc import DALC_getbookbyisbn

def DB_GetBookbyISBN(isbn):
    try:
        libro = DALC_getbookbyisbn(isbn)
        return libro
    except ObjectDoesNotExist:
         raise f"Error en DALC_GetusuariobyUser -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en DALC_GetusuariobyUser -> {MultipleObjectsReturned}"