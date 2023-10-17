from django.shortcuts import render

def home_login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
