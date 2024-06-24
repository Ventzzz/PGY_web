from django.urls import path

from . import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("registro/", views.registro, name="registro"),
]