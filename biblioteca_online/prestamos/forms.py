# en forms.py
from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['id_usuario', 'id_ejemplar', 'fecha_iniprestamo', 'fecha_finprestamo', 'fecha_devolucion']
