from .forms import RegisterForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home_page(request):
    return render(request,'home.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user:
            login(request,user)
            return redirect('/bibliotinka')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        return render(request,'login.html')

def logout_user(request):
    pass

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/bibliotinka')
    else:
        form = RegisterForm()
    return render(request,'registration/sign_up.html',{'form':form})
