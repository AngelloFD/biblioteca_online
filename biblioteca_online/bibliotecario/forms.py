# En tu archivo forms.py
from django import forms
import requests
from core.models import Libro
from prestamos.models import Ejemplares
from prestamos.models import Prestamo

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['categoria', 'title', 'author', 'isbn', 'summary', 'image']
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')

        if not title or not author:
            raise forms.ValidationError('Los campos de título y autor son obligatorios.')
        
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        print(f"ISBN a validar: {isbn}")

        # Verifica la existencia de un libro con el mismo ISBN en el catálogo
        if Libro.objects.filter(isbn=isbn).exists():
            print("¡Libro con ISBN existente encontrado!")
            raise forms.ValidationError('Ya existe un libro con este ISBN en el catálogo.')

        # Realiza la validación del ISBN utilizando la API de Open Library
        response = requests.get(f'https://openlibrary.org/isbn/{isbn}.json')
        if response.status_code != 200:
            raise forms.ValidationError('El ISBN ingresado es inválido. Proporcione un ISBN válido.')

        return isbn

class EjemplarForm(forms.ModelForm):
    class Meta:
        model = Ejemplares
        fields = ['libro', 'estado', 'resumen', 'compuesto']
        widgets = {
            'libro': forms.Select(attrs={'required': 'true'}),
            'estado': forms.Select(attrs={'required': 'true'}),
            'resumen': forms.Textarea(attrs={'required': 'true'}),
            'compuesto': forms.TextInput(attrs={'required': 'true'}),
        }

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['id_usuario', 'id_ejemplares', 'prestado_estado', 'fecha_iniprestamo', 'fecha_finprestamo', 'fecha_devolucion']
        widgets = {
            'id_usuario': forms.Select(attrs={'required': 'true'}),
            'id_ejemplares': forms.TextInput(attrs={'required': 'true'}),
            'prestado_estado': forms.Select(attrs={'required': 'true'}),
            'fecha_iniprestamo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_finprestamo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }