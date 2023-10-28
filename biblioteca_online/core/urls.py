from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
   path('', views.core_home, name="core_home"),
   path('main', views.main_frontend, name="frontendmain"),
   path('bookdetail', views.bookdetail_frontend, name="bookdetailmain"),
]