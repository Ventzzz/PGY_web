from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("registro/", views.registro, name="registro"),
    path('carrito/', views.carrito, name='carrito'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('agregar_al_carrito/<int:id_bebida>/', views.agregar_al_carrito, name='agregar_al_carrito'),
]