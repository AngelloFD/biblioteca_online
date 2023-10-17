from datetime import timezone
from django.shortcuts import render

def home_login(request):
    return render(request,'login.html')

def header_footer(request):
    return render(request,'headerFoot.html')

def registroAdm(request):
    return render(request,'registroAdm.html')
