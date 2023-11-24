from django.shortcuts import render
from .models import Prestamo, Ejemplares


def detalle_prestamo(request, id_prestamo):
    prestamo = Prestamo.objects.get(id_prestamo=id_prestamo)
    ejemplares_ids = prestamo.id_ejemplares.split(',')  # Asume que los ids de los ejemplares están separados por comas
    ejemplares = Ejemplares.objects.filter(id_ejemplar__in=ejemplares_ids)
    return render(request, 'prestamos/detalle-prestamo.html', {'prestamo': prestamo, 'ejemplares': ejemplares})

