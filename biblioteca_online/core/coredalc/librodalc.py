from core.models import Libro
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def DALC_getbookbyisbn(isbn) -> Libro:
    try:
        if isbn == 0:
            raise ObjectDoesNotExist
        libros:Libro
        libros = Libro.objects.get(isbn=isbn)
        return libros
    except ObjectDoesNotExist:
        raise f"Error en DALC_GetusuariobyUser -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en DALC_GetusuariobyUser -> {MultipleObjectsReturned}"