from django.http import JsonResponse
from django.shortcuts import render
from usuario.usuariobc.usuariobc import BC_CheckUsuarioDNI,BC_GetusuariobyUser
from core.models import Libro
from prestamos.models import Ejemplares


# Create your views here.
def main_frontend(request):
    dni_check:bool
    dni_check = False
    """
    if request.user.is_authenticated:
        if BC_CheckUsuarioDNI(BC_GetusuariobyUser(request.user)):
            dni_check = True
    """
    libros = Libro.objects.all()
    ejemplares_count = {
        libro.isbn: Ejemplares.objects.filter(libro=libro,estado="1").count() for libro in libros
    }
    if "carrito" not in request.session:
        request.session["carrito"] = []
    context = {
        "libros": libros,
        "carrito": request.session["carrito"],
        "ejemplares_count": ejemplares_count,
        "dni_check": dni_check,
    }

    return render(request, "core/store_mainpage/main_frontend.html", context)


def add_book(request):
    isbn_libro = request.GET.get("isbn")
    carrito = request.session.get("carrito", [])
    carrito.append(isbn_libro)
    request.session["carrito"] = carrito
    return JsonResponse({"num_items": len(carrito)})


def bookdetail_frontend(request):
    return render(request, "core/store_mainpage/main_bookdetail.html")
