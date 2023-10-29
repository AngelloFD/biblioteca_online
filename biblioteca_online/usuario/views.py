from .forms import RegisterForm, LoginForm
from .models import Usuario
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

# Create your views here.
def update_user_data(user):
    Usuario.objects.filter(user=user).update(
        dni=user.dni,
        fecha_nacimiento=user.fecha_nacimiento,
        compuesto=user.compuesto,
        fecha_actualizacion=user.fecha_actualizacion,
    )

def home_page(request):
    return render(request,'home.html')

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                login(request,user)
                return redirect('core:frontendmain')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
                return render(request,'registration/login.html', {'form' : form})
    else:
        form = LoginForm()
        return render(request,'registration/login.html', {'form' : form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            
            user.save()
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=user.username, password=raw_password)
            if user:
                login(request,user)
                return redirect('core:frontendmain')
    else:
        form = RegisterForm()
    return render(request,'registration/sign_up.html',{'form':form})
