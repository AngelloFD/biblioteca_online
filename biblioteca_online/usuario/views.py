from .forms import RegisterForm, LoginForm
from .services import verificar_DNI
from .models import Usuario
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import ensure_csrf_cookie

# @ensure_csrf_cookie -> fuerza que se actualice el csrf token

# Create your views here.


def home_page(request):
    return render(request, "usuario/home.html")


@ensure_csrf_cookie
def login_user(request):
    if request.user.is_authenticated:
        return redirect("core:frontendmain")
    # TO-DO: Investigar si sería necesario forzar un logout aquí
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("core:frontendmain")
            else:
                messages.success(request, "Usuario o contraseña incorrectos")
                return render(
                    request, "usuario/registration/login.html", {"form": form}
                )
        else:
            messages.success(request, f"{form.errors}")
    else:
        form = LoginForm()
        print(form.errors)
        return render(request, "usuario/registration/login.html", {"form": form})


@ensure_csrf_cookie
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.save()
            raw_password = form.cleaned_data.get("password1")

            user = authenticate(username=user.username, password=raw_password)
            if user:
                login(request, user)
                return redirect("core:frontendmain")
        else:
            messages.success(request, f"{form.errors}")
    else:
        form = RegisterForm()
    return render(request, "usuario/registration/sign_up.html", {"form": form})


def logout_user(request):
    request.session.flush()  # Es necesario?
    logout(request)
    return redirect("usuario:welcome_page")


@ensure_csrf_cookie
def conf_user(request):
    if request.method == "POST":
        dni = request.POST.get("dni")
        print("dni: ", dni)
        if dni is None:
            return render(request, "usuario/confUser.html")
        result = verificar_DNI(dni)
        print("result: ", result)
        if result and 'nombres' in result:
            # agregar first_name, last_name y dni al usuario
            user = request.user
            user.first_name = result["nombres"]
            user.last_name = result["apellidoPaterno"] + " " + result["apellidoMaterno"]
            try:
                user.usuario
            except ObjectDoesNotExist:
                Usuario.objects.create(user=user)
            print(user.usuario.dni)
            user.usuario.dni = result["numeroDocumento"]
            user.usuario.save()
            user.save()
            messages.success(request, "Datos actualizados correctamente")
            # return redirect("core:frontendmain")
            return render(request, "usuario/confUser.html", {"result": result})
        else:
            messages.error(request, "DNI no válido")
            return render(request, "usuario/confUser.html")
    else:
        return render(request, "usuario/confUser.html")

def solicitud_user(request):
    if request.user.is_authenticated:
        return render(request, "usuario/solicitudUser.html")
    else:
        return render(request, "usuario/login.html")
