from django.http import HttpResponseNotFound, JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from core.utils.core_utils import CheckUserDNI
from core.corebc.librobc import DB_GetBookbyISBN
from core.models import Libro
from prestamos.models import Ejemplares


# Create your views here.
def main_frontend(request):
    libros = Libro.objects.all().order_by("isbn")
    paginator = Paginator(libros, 8)
    page_number = request.GET.get("page")
    libros_pag = paginator.get_page(page_number)
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
        "dni_check": dni_check,
        "libros_pag": libros_pag,
    }
    return render(request, "core/store_mainpage/main_frontend.html", context)


def add_book(request):
    isbn_libro = request.GET.get("isbn_libro")
    print(f"Dato a agregar: {isbn_libro}")
    carrito = request.session.get("carrito", [])
    carrito.append(isbn_libro)
    request.session["carrito"] = carrito
    return JsonResponse({"num_items": len(carrito), "in_cart": True})

def eliminar_libro(request):
    isbn_libro = request.POST.get('isbn_libro')
    print(f"Dato a eliminar: {isbn_libro}")
    carrito = request.session.get('carrito', [])
    carrito = [item for item in carrito if item['isbn'] != isbn_libro]
    request.session['carrito'] = carrito
    return JsonResponse({'success': True})

def print_carrito(request, timestamp):
    carrito = request.session.get("carrito", [])
    lista:list
    lista = []
    for item in carrito:
        libro:Libro
        libro = DB_GetBookbyISBN(item)
        lista.append({'isbn': libro.isbn, 'titulo': libro.title})
    return JsonResponse({'carrito_detalle': lista})


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
