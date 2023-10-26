from django.shortcuts import render

# Create your views here.
def core_home(request):
   return render(request,'core_home.html')
