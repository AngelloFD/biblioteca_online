from django.urls import path, include
from . import views

app_name = "usuario"

urlpatterns = [
   path('login/', views.login_user, name="user_login"),
   path('logingout/', views.logout_user, name="user_logout"),
   path('register', views.register, name="user_register"),
   path('', views.home_page, name="welcome_page"),
   path('confUser/', views.conf_user, name="configure_page"),
]
