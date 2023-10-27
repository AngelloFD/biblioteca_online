from django.urls import path, include
from . import views

urlpatterns = [
   path('login', views.login, name="user_login"),
   path('register', views.register, name="user_register"),
   path('logout', views.register, name="user_logout"),
   path('', views.home_page, name="welcome_page"),
   #path('bibliotinka', include('core.urls')),
]
