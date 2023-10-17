"""
URL configuration for biblioteca_online project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home_login, name="login_usuario"),
    path('register', views.register, name="register_usuario"),
<<<<<<< HEAD
=======
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('confirmacion_agregar_libro/', views.confirmacion_agregar_libro, name='confirmacion_agregar_libro'),
    path('registrar_prestamo/<int:libro_id>/', views.registrar_prestamo, name='registrar_prestamo'),
    path('confirmacion_prestamo/', views.confirmacion_prestamo, name='confirmacion_prestamo'),
    path('libro_prestado/', views.libro_prestado, name='libro_prestado'),
    path('registrar_devolucion/<int:libro_id>/', views.registrar_devolucion, name='registrar_devolucion'),
    path('confirmacion_devolucion/', views.confirmacion_devolucion, name='confirmacion_devolucion'),
    path('libro_disponible/', views.libro_disponible, name='libro_disponible'),
>>>>>>> ea29b3da44b7b6887bb72ce7a37f248f75e8d03a
]
