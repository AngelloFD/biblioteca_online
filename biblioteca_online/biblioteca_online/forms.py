from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'disponible', 'fecha_prestamo', 'fecha_vencimiento', 'prestado_a']