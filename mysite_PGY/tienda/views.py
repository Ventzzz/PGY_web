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

def carrito(request):
    carrito = request.session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    contexto = {
        'carrito': carrito,
        'total': total
    }
    return render(request, 'tienda/carroDeCompras.html', contexto)

def agregar_al_carrito(request, id_bebida):
    bebida = Bebidas.objects.get(id=id_bebida)
    carrito = request.session.get('carrito', [])
    
    for item in carrito:
        if item['id'] == bebida.id:
            item['cantidad'] += 1
            break
    else:
        carrito.append({
            'id': bebida.id,
            'nombre': bebida.nombre,
            'precio': bebida.precio,
            'cantidad': 1,
            'imagen': bebida.imagen.url if bebida.imagen else None
        })
    
    request.session['carrito'] = carrito
    
    if 'from_cart' in request.POST:
        return redirect('/tienda/carrito')
    return redirect('/tienda/catalogo')

def producto(request, id_bebida):
    bebida = Bebidas.objects.get(id=id_bebida)
    contexto = {"bebida" : bebida}

    return render(request, 'tienda/producto.html', contexto)