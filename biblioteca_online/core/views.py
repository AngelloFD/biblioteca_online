from django.http import JsonResponse
from django.shortcuts import render
from core.models import Libro
from prestamos.models import Ejemplares


# Create your views here.
def main_frontend(request):
    libros = Libro.objects.all()
    ejemplares_count = {
        libro.isbn: Ejemplares.objects.filter(libro=libro).count() for libro in libros
    }
    if "carrito" not in request.session:
        request.session["carrito"] = []
    context = {
        "libros": libros,
        "carrito": request.session["carrito"],
        "ejemplares_count": ejemplares_count,
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
