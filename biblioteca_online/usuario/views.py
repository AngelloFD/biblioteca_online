import secrets
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from prestamos.prestamosbc.prestamosBC import BC_GetPrestamoOfUsuario
from usuario.usuariobc.usuariobc import BC_GetusuariobyUser
from .forms import RegisterForm, LoginForm
from .services import verificar_DNI
from .models import Usuario, verificar_correo
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import ensure_csrf_cookie

# @ensure_csrf_cookie -> fuerza que se actualice el csrf token

User = get_user_model()
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
                usuario = BC_GetusuariobyUser(user)
                if usuario.email_verificado:
                    login(request, user)
                    return redirect("core:frontendmain")
                else:
                    messages.success(request, "Porfavor verifica tu correo")
                    return render(
                        request, "usuario/registration/login.html", {"form": form}
                    )
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
    global usuarios
    global id_usuario
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get("email")

            if verificar_correo(user.email):
                user.save()
                user.refresh_from_db()

                # Envía el correo de confirmación
                # Genera y guarda el token en el usuario
                token = generar_token()

                # Actualiza el modelo Usuario con el token generado
                usuario = Usuario.objects.get(user=user)
                usuario.email_confirmation_token = token
                usuario.save()

                enviar_correo_confirmacion(user.email, token)

                # Redirige a la página de confirmación de correo electrónico
                return redirect("usuario:informacion_registro")

            else:
                messages.error(request, "Correo electrónico no válido.")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = RegisterForm()
    return render(request, "usuario/registration/sign_up.html", {"form": form})

def generar_token():
    # Genera un token seguro usando secrets.token_urlsafe
    return secrets.token_urlsafe(32)

def enviar_correo_confirmacion(email, token):
    # Genera la URL de confirmación utilizando reverse
    # http://127.0.0.1:8000/
    confirm_url = "http://127.0.0.1:8000" + reverse("usuario:confirmar_email") + f"?token={token}"

    subject = "Confirmación de correo electrónico"
    # Incluye la URL de confirmación en el mensaje
    message = f"¡Gracias por registrarte! Por favor, haz clic en el siguiente enlace para verificar tu dirección de correo electrónico: {confirm_url}"
    from_email = settings.EMAIL_HOST_USER  # Utiliza la dirección de correo electrónico configurada en settings.py
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

def informacion_registro(request):
    return render(request, 'usuario/informacion_registro.html')

def confirmar_email(request):
    # Verificar si el token de confirmación está presente en la solicitud
    token = request.GET.get('token')
    if not token:
        return HttpResponseBadRequest("Falta el token de confirmación en la URL.")
    
    try:
        # Realiza la consulta a través del modelo Usuario
        usuario = Usuario.objects.get(email_confirmation_token=token)
        # Marcar el correo electrónico como confirmado y guardar el usuario
        usuario.email_verificado = True
        usuario.save()

        messages.success(request, "¡Tu correo electrónico ha sido confirmado con éxito!")
        
        # Autenticar al usuario y redirigir según la lógica de tu aplicación
        user = authenticate(username=usuario.user.username, password=usuario.user.password)
        if user:
            login(request, user)
            if user.is_staff:
                # Redirigir al dashboard del bibliotecario
                if user.is_superuser:
                    return redirect("core:frontendmain")
                else:
                    return redirect("bibliotecario:dashboardBooker")
            else:
                return redirect("core:frontendmain")
        else:
            error_message = f"Error al autenticar al usuario. Credenciales: {usuario.user.username}/{usuario.user.password}"
            messages.error(request, error_message)
            return redirect("usuario:welcome_page")
    except Usuario.DoesNotExist:
        return HttpResponseBadRequest("Token de confirmación no válido.")


def logout_user(request):
    request.session.flush()  # Es necesario?
    logout(request)
    return redirect("usuario:welcome_page")


@ensure_csrf_cookie
def conf_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            dni = request.POST.get("dni")
            print("dni: ", dni)
            if dni is None:
                return render(request, "usuario/confUser.html")
            result = verificar_DNI(dni)
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
    else:
        return redirect("usuario:user_login")

@ensure_csrf_cookie
def cambiar_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña cambiada exitosamente.')
            return redirect('usuario:configure_page')
        else:
            messages.error(request, 'Hubo un error al cambiar la contraseña. Por favor, corrige los errores en el formulario.')
            return render(request, 'usuario/cambiar_password.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'usuario/cambiar_password.html', {'form': form})
    
@user_passes_test(lambda u: u.is_authenticated, login_url='usuario:user_login')
@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        # Verificar la contraseña del usuario antes de eliminar la cuenta
        password = request.POST.get('password')
        if request.user.check_password(password):
            # Confirmación de eliminación
            return render(request, 'usuario/confirmar_eliminar_cuenta.html')
        else:
            messages.error(request, 'Contraseña incorrecta. Inténtalo de nuevo.')

    return render(request, 'usuario/eliminar_cuenta.html')

@user_passes_test(lambda u: u.is_authenticated, login_url='usuario:user_login')
@login_required
def confirmar_eliminar_cuenta(request):
    if request.method == 'POST':
        # Eliminar la cuenta del usuario
        request.user.delete()
        logout(request)
        messages.success(request, 'Tu cuenta ha sido eliminada con éxito.')
        return redirect('core:frontendmain')  # Puedes redirigir a donde desees después de la eliminación
    else:
        return redirect('usuario:eliminar_cuenta')

def solicitud_user(request):
    if request.user.is_authenticated:
        usuario:Usuario
        usuario = BC_GetusuariobyUser(request.user)
        prestamos = BC_GetPrestamoOfUsuario(usuario)
        context = {
            "prestamos": prestamos
        }
        return render(request, "usuario/solicitudUser.html",context)
    else:
        return redirect("usuario:user_login")
