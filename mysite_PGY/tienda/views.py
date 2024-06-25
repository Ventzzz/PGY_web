from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages
from tienda.forms import ProductoForm, RegistrationForm
from .models import Bebidas
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

# Ex: localhost:8000/tienda/inicio/
def inicio(request):
    objetos = Bebidas.objects.all()
    contexto = {"bebidas" : objetos}
    return render(request,"tienda/inicio.html", contexto)

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


def loginV(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Estas loggeado {username}.")
                return redirect('inicio')
            else:
                messages.error(request, "Esta incorrecto el username o contraseña.")
        else:
            messages.error(request, "no es correcto el username o contraseña.")
    form = AuthenticationForm()
    return render(request, 'tienda/login.html', {'form': form})

def actualizar_producto(request, id_bebida):
    bebida = get_object_or_404(Bebidas, id=id_bebida)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=bebida)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('inicio')  # Redirige a una vista de detalle del producto u otra vista
    else:
        form = ProductoForm(instance=bebida)
    
    return render(request, 'tienda/actualizar_producto.html', {'form': form, 'producto': bebida})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado exitosamente.')
            return redirect('inicio')  # Redirige a la lista de productos u otra vista
    else:
        form = ProductoForm()
    
    return render(request, 'tienda/agregar_producto.html', {'form': form})

def eliminar_producto(request, id_bebida):
    producto = get_object_or_404(Bebidas, id=id_bebida)
    
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('inicio')  # Redirige a la lista de productos u otra vista
    
    return render(request, 'tienda/eliminar_producto.html', {'producto': producto})