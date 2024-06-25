from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("registro/", views.registro, name="registro"),
    path('carrito/', views.carrito, name='carrito'),
    path('producto/<int:id_bebida>', views.producto, name='producto'),
    path('agregar_al_carrito/<int:id_bebida>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('login/', views.loginV, name='login'),
    path('actualizar_producto/<int:id_bebida>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar_producto/<int:id_bebida>/', views.eliminar_producto, name='eliminar_producto'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)