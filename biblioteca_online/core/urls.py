from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
   path('main', views.main_frontend, name="frontendmain"),
   path('main/bookdetail', views.bookdetail_frontend, name="bookdetailmain"),
   path('main/prestamo/', include('prestamos.urls')),
]