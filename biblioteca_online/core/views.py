from django.http import JsonResponse
from django.shortcuts import render
from prestamos.models import Ejemplares
# Create your views here.
def main_frontend(request):
   ejemplares = Ejemplares.objects.all()
   context = {"ejemplares" : ejemplares}
   if 'carrito' not in request.session:
      request.session['carrito'] = []
   return render(request,'core/store_mainpage/main_frontend.html', context)

def add_book(request):
   isbn_libro = request.GET.get('isbn')
   carrito = request.session.get('carrito', [])
   carrito.append(isbn_libro)
   request.session['carrito'] = carrito
   return JsonResponse({'num_items': len(carrito)})

def bookdetail_frontend(request):
   return render(request,'core/store_mainpage/main_bookdetail.html')