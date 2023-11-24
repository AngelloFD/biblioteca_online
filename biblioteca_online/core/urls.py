from django.urls import path, include
from . import views
app_name = "core"

urlpatterns = [
   path('main/', views.main_frontend, name="frontendmain"),
   path('main/bookdetail/<str:isbn>/', views.bookdetail_frontend, name="bookdetailmain"),
   path('main/prestamo/', include('prestamos.urls')),
   # links que manejan solicitudes del carrito
   path('add_book/', views.add_book, name='add_book'),
   path('crear_solicitud/', views.crear_prestamo, name='crear_solicitud'),
   path('eliminar_libro/', views.eliminar_libro, name='eliminar_libro'),
   path('print_carrito/<int:timestamp>/', views.print_carrito, name='print_carritos'),
]