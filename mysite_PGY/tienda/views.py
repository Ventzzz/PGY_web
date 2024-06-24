from django.shortcuts import redirect, render
from django.http import HttpResponse

from tienda.forms import RegistrationForm
from .models import Bebidas

# Create your views here.

# Ex: localhost:8000/tienda/inicio/
def inicio(request):
    return render(request,"tienda/inicio.html",{})

def catalogo(request):
    objetos = Bebidas.objects.all()
    contexto = {"bebidas" : objetos}
    return render(request, "tienda/catalogo.html", contexto)

def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tienda/inicio')
    else:
        form = RegistrationForm()
    
    return render(request, 'tienda/registro.html', {'form': form})