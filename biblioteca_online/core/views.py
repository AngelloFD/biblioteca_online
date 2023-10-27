from django.shortcuts import render

# Create your views here.
def core_home(request):
   return render(request,'core_home.html')

def main_frontend(request):
   return render(request,'core/store_mainpage/main_frontend.html')

def bookdetail_frontend(request):
   return render(request,'core/store_mainpage/main_bookdetail.html')