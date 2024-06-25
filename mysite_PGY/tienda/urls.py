from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("registro/", views.registro, name="registro"),
    path('carrito/', views.carrito, name='carrito'),
    path('producto/<int:id_bebida>', views.producto, name='producto'),
    path('agregar_al_carrito/<int:id_bebida>/', views.agregar_al_carrito, name='agregar_al_carrito'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)