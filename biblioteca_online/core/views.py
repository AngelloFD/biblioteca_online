from datetime import date, timedelta
from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from prestamos.prestamosbc.prestamosBC import BC_crearPrestamo
from usuario.usuariobc.usuariobc import BC_GetusuariobyUser
from core.utils.core_utils import CheckUserDNI
from core.corebc.librobc import DB_GetBookbyISBN
from core.models import Libro
from prestamos.models import Ejemplares


# Create your views here.
def main_frontend(request):
    query = request.GET.get("search")
    if query:
        libros = Libro.objects.filter(title__icontains=query).order_by("isbn")
    else:
        libros = Libro.objects.all().order_by("isbn")
    paginator = Paginator(libros, 8)
    page_number = request.GET.get("page")
    libros_pag = paginator.get_page(page_number)
    dni_check: bool
    dni_check = False
    if request.user.is_authenticated:
        dni_check = CheckUserDNI(request.user)

    ejemplares_count = {
        libro.isbn: Ejemplares.objects.filter(libro=libro, estado="1").count()
        for libro in libros
    }
    if "carrito" not in request.session:
        request.session["carrito"] = []
    context = {
        "libros": libros,
        "carrito": request.session["carrito"],
        "ejemplares_count": ejemplares_count,
        "dni_check": dni_check,
        "libros_pag": libros_pag,
    }

    return render(request, "core/store_mainpage/main_frontend.html", context)

def add_book(request):
    isbn_libro = request.GET.get("isbn_libro")
    print(f"Dato a agregar: {isbn_libro}")
    carrito = request.session.get("carrito", [])
    
    # Verificar si el libro ya está en el carrito
    if isbn_libro in carrito:
        return HttpResponseBadRequest("El libro ya está en la bandeja")

    carrito.append(isbn_libro)
    request.session["carrito"] = carrito

    # Obtener detalles del libro recién agregado
    libro = DB_GetBookbyISBN(isbn_libro)
    libro_info = {"isbn": libro.isbn, "titulo": libro.title}


    return JsonResponse({"num_items": len(carrito), "in_cart": True, "libro_info": libro_info})


def eliminar_libro(request):
    isbn_libro = request.POST.get("isbn_libro")
    print(f"Dato a eliminar: {isbn_libro}")
    carrito = request.session.get("carrito", [])
    carrito = [item for item in carrito if item["isbn"] != isbn_libro]
    request.session["carrito"] = carrito
    return JsonResponse({"success": True})


def print_carrito(request, timestamp):
    carrito = request.session.get("carrito", [])
    lista: list
    lista = []
    for item in carrito:
        libro: Libro
        libro = DB_GetBookbyISBN(item)
        lista.append({"isbn": libro.isbn, "titulo": libro.title})
    return JsonResponse({"carrito_detalle": lista})

def carrito_vacio(request):
    if "carrito" in request.session:
        del request.session["carrito"]
        request.session.save()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})  
    
def crear_prestamo(request):
    isbns = request.session.get("carrito", [])
    lista = []
    for isbn in isbns:
        local = DB_GetBookbyISBN(isbn)
        lista.append(local)
    id_ejemplares:str
    for item in lista:
        id_ejemplares = item + ','
    cadena_sin_ultimo_digito = id_prestamo[:-1]
    print(cadena_sin_ultimo_digito)
    id_ejemplares = cadena_sin_ultimo_digito
    prestado_estado = 'En espera'
    usuario = BC_GetusuariobyUser(request.user)
    id_usuario = usuario.id
    id_prestamo = request.user.id + date.today()
    fecha_iniprestamo = date.today()
    fecha_actual = date.today()
    fecha_finprestamo = fecha_actual + timedelta(days=20)
    fecha_devolucion = None
    if BC_crearPrestamo(id_prestamo,id_ejemplares,id_usuario,prestado_estado,fecha_iniprestamo,fecha_finprestamo,fecha_devolucion):
        if "carrito" in request.session:
            del request.session["carrito"]
            request.session.save()
        return main_frontend(request)
    return carrito_vacio(request)

def bookdetail_frontend(request, isbn):
    libro: Libro
    libro = DB_GetBookbyISBN(isbn)
    if libro is None:
        return HttpResponseNotFound("No se encontró el libro")

    dni_check: bool
    dni_check = False
    if request.user.is_authenticated:
        dni_check = CheckUserDNI(request.user)

    ejemplares_count = {
        libro.isbn: Ejemplares.objects.filter(libro=libro, estado="1").count()
    }
    if "carrito" not in request.session:
        request.session["carrito"] = []
    context = {
        "carrito": request.session["carrito"],
        "dni_check": dni_check,
        "libro": libro,
        "ejemplares_count": ejemplares_count,
    }
    return render(request, "core/store_mainpage/main_bookdetail.html", context)

