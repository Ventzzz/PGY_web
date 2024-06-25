from django.urls import path

from . import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("registro/", views.registro, name="registro"),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar_al_carrito/<int:id_bebida>/', views.agregar_al_carrito, name='agregar_al_carrito'),
]