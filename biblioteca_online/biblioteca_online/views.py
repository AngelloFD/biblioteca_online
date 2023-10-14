from django.shortcuts import render

def home_login(request):
    return render(request,'login.html')