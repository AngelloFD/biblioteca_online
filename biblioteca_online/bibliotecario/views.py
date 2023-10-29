from django.shortcuts import render

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