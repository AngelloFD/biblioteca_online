from django.shortcuts import render

# Create your views here.
def prestamo_frontend(request):
   return render(request,'prestamos/main_prestamo.html')