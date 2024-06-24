from django.contrib import admin

# Register your models here.

from .models import Bebidas,Usuario

admin.site.register(Bebidas)
admin.site.register(Usuario)