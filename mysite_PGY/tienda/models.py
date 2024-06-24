from django.db import models

# Create your models here.

class Usuario(models.Model):
    user = models.CharField(max_length=25)
    password = models.CharField(max_length=50)

class Bebidas(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='bebida_Imagen/',)
    def __str__(self):
        return self.nombre