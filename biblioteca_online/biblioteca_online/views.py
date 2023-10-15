from django.shortcuts import render

def home_login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

from django.shortcuts import render, redirect
from .forms import LibroForm

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion_agregar_libro')  # Redirige a la página de confirmación
    else:
        form = LibroForm()
    
    return render(request, 'agregar_libro.html', {'form': form})

def confirmacion_agregar_libro(request):
    return render(request, 'confirmacion_agregar_libro.html')

"@login_required"
def registrar_prestamo(request, libro_id):
    libro = Libro.objects.get(pk=libro_id)
    
    if libro.disponible:
        libro.disponible = False
        libro.fecha_prestamo = timezone.now()
        libro.fecha_vencimiento = timezone.now() + timezone.timedelta(days=30)  # Ejemplo de 30 días de préstamo
        libro.prestado_a = request.user
        libro.save()
        return redirect('confirmacion_prestamo')
    else:
        # El libro ya está prestado, maneja esta situación en tu plantilla
        return render(request, 'libro_prestado.html', {'libro': libro})

def confirmacion_prestamo(request):
    return render(request, 'confirmacion_prestamo.html')