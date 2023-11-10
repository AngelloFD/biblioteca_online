from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from core.utils.core_utils import CheckUserDNI
from core.corebc.librobc import DB_GetBookbyISBN
from core.models import Libro
from prestamos.models import Ejemplares


# Create your views here.
def main_frontend(request):

    libros = Libro.objects.all()
    dni_check:bool 
    dni_check = False
    if request.user.is_authenticated:
        dni_check = CheckUserDNI(request.user)

    ejemplares_count = {
        libro.isbn: Ejemplares.objects.filter(libro=libro,estado="1").count() for libro in libros
    }
    if "carrito" not in request.session:
        request.session["carrito"] = []
    context = {
        "libros": libros,
        "carrito": request.session["carrito"],
        "ejemplares_count": ejemplares_count,
        "dni_check": dni_check
    }
    return render(request, "core/store_mainpage/main_frontend.html", context)


def add_book(request):
    isbn_libro = request.GET.get("isbn")
    carrito = request.session.get("carrito", [])
    carrito.append(isbn_libro)
    request.session["carrito"] = carrito
    return JsonResponse({"num_items": len(carrito)})


def bookdetail_frontend(request, isbn):
    libro:Libro
    libro = DB_GetBookbyISBN(isbn)
    if libro is None:
        return HttpResponseNotFound("No se encontró el libro")  
    
    dni_check:bool 
    dni_check = False
    if request.user.is_authenticated:
        dni_check = CheckUserDNI(request.user)

    ejemplares_count = {
        libro.isbn: Ejemplares.objects.filter(libro=libro,estado="1").count()
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
