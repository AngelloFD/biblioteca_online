from django.shortcuts import render
from prestamos.models import Ejemplares

# Create your views here.
def main_frontend(request):
   ejemplares = Ejemplares.objects.all()
   context = {"ejemplares" : ejemplares}
   return render(request,'core/store_mainpage/main_frontend.html', context)

def bookdetail_frontend(request):
   return render(request,'core/store_mainpage/main_bookdetail.html')