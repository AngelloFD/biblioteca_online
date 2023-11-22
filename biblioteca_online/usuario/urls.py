from django.urls import path, include
from . import views

app_name = "usuario"

urlpatterns = [
   path('login/', views.login_user, name="user_login"),
   path('logingout/', views.logout_user, name="user_logout"),
   path('register', views.register, name="user_register"),
   path('', views.home_page, name="welcome_page"),
   path('confUsuario/', views.conf_user, name="configure_page"),
   path('soliUser/', views.solicitud_user, name="solicitud_user"),
   path('confirmar_email/', views.confirmar_email, name='confirmar_email'),
   path('informacion_registro/', views.informacion_registro, name='informacion_registro'),
   path('cambiar_password/', views.cambiar_password, name='cambiar_password'),
   path('eliminar-cuenta/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('confirmar-eliminar-cuenta/', views.confirmar_eliminar_cuenta, name='confirmar_eliminar_cuenta'),
]
