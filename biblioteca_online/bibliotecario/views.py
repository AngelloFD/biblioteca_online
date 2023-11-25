import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import LibroForm
from .forms import EjemplarForm
from .forms import PrestamoForm
from core.models import Libro
from usuario.models import Usuario
from core.models import Estado
from prestamos.models import Ejemplares
from prestamos.models import Prestamo
from django.contrib.auth.decorators import login_required

# Create your views here.
def panel_bibliotecario(request):
    # Obtener todas las solicitudes de préstamo
    #solicitudes = SolicitudPrestamo.objects.all()
    
    # Implementa la lógica de búsqueda si es necesario
    #query = request.GET.get('q')
    #if query:
    #    solicitudes = solicitudes.filter(libro__titulo__icontains=query)
    
    return render(request, 'panel_bibliotecario.html')

def libros(request):
    return render (request, 'libros.html')

def prestamos(request):
    return render (request, 'prestamos.html')

# Lo de arriba esta por borrarse, aun no se hace pq puede ocasionar perjuicios al codigo

def dashboard_booker(request):
    libros = Libro.objects.all()  # Obtén todos los registros de libros

    context = {
        'libros': libros,
    }

    return render(request, 'bibliotecario/dashboardBooker.html', context)

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            nuevo_libro = form.save()
            return render(request, 'bibliotecario/confirmacion.html', {'libro': nuevo_libro})
    else:
        form = LibroForm()

    return render(request, 'bibliotecario/agregar_libro.html', {'form': form})

def registrar_ejemplar(request):
    if request.method == 'POST':
        form = EjemplarForm(request.POST)
        if form.is_valid():
            # Obtén el libro seleccionado en el formulario
            libro = form.cleaned_data['libro']

            # Guarda el formulario para obtener el ID generado automáticamente
            ejemplar = form.save(commit=False)

            # Establece el estado y el ID del ejemplar según el estado seleccionado
            estado = form.cleaned_data['estado']
            if estado.nombre == 'Reservado':
                ejemplar.id_ejemplar = f"{libro.title}2"
                ejemplar.estado = Estado.objects.get(nombre='Reservado')
            elif estado.nombre == 'Prestado':
                ejemplar.id_ejemplar = f"{libro.title}3"
                ejemplar.estado = Estado.objects.get(nombre='Prestado')
            elif estado.nombre == 'De baja':
                ejemplar.id_ejemplar = f"{libro.title}4"
                ejemplar.estado = Estado.objects.get(nombre='De baja')
            else:  # Default: 'Disponible'
                ejemplar.id_ejemplar = f"{libro.title}1"
                ejemplar.estado = Estado.objects.get(nombre='Disponible')

            # Guarda el ejemplar con el ID actualizado
            ejemplar.save()

            # Puedes realizar otras acciones aquí si es necesario
            return render(request, 'bibliotecario/confirmacionEjemplar.html', {'mensaje': 'Ejemplar registrado con éxito'})
    else:
        form = EjemplarForm()

    return render(request, 'bibliotecario/registrar_ejemplar.html', {'form': form})

def registrar_prestamo(request):
    # Obtener la fecha actual
    fecha_actual = datetime.date.today()

    # Obtener ejemplares disponibles desde la base de datos
    ejemplares_disponibles = Ejemplares.objects.filter(estado__nombre='Disponible')

    # Obtener usuarios desde la base de datos
    usuarios = Usuario.objects.all()

    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)

            # Obtener el nombre de usuario del usuario seleccionado
            usuario_seleccionado = form.cleaned_data['id_usuario']

            # Generar el ID de préstamo automáticamente
            prestamo.id_prestamo = f"{usuario_seleccionado.user.username}{fecha_actual}"

            prestamo.id_ejemplares = form.cleaned_data['id_ejemplares']
            prestamo.save()

            # Actualizar el estado del ejemplar a "prestado"
            ejemplares_ids = [id.strip() for id in prestamo.id_ejemplares.split(',')]
            for ejemplar_id in ejemplares_ids:
                ejemplar = Ejemplares.objects.get(id_ejemplar=ejemplar_id)
                ejemplar.estado = Estado.objects.get(nombre='Reservado')
                ejemplar.save()

            # Imprimir los parámetros del formulario en la consola
            print(f"Prestamo registrado: {prestamo.id_prestamo}, Ejemplares: {prestamo.id_ejemplares}")
            return render(request, 'bibliotecario/confirmacionGeneral.html')  # Ajusta la redirección según tus necesidades
    else:
        form = PrestamoForm()
        
    return render(request, 'bibliotecario/registrar_prestamo.html', {'form': form, 'ejemplares_disponibles': ejemplares_disponibles, 'usuarios': usuarios, 'fecha_actual': fecha_actual})

def visualizar_prestamos(request):
    # Obtener todos los préstamos de la base de datos
    prestamos = Prestamo.objects.all()

    # Lógica para manejar la búsqueda por ID de usuario
    if 'id_usuario' in request.GET:
        id_usuario = request.GET['id_usuario']
        prestamos = prestamos.filter(id_usuario__id=id_usuario)

    return render(request, 'bibliotecario/visualizar_prestamos.html', {'prestamos': prestamos})

def modificar_estado_prestamo(request, id_prestamo):
    # Obtener el préstamo seleccionado
    prestamo = get_object_or_404(Prestamo, id_prestamo=id_prestamo)

    # Lógica para procesar el formulario de modificación
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('bibliotecario/visualizar_prestamos.html')
    else:
        form = PrestamoForm(instance=prestamo)

    return render(request, 'bibliotecario/modificar_estado_prestamo.html', {'form': form})