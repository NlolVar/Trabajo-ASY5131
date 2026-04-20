from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Carrito, ItemCarrito
from productos.models import Producto

@login_required
def ver_carrito(request):
    # Obtener el carrito del usuario o crear uno si no existe
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    # Obtener todos los items del carrito
    items = carrito.items.all()
    
    # Calcular el total
    total = sum(item.producto.precio * item.cantidad for item in items)
    
    return render(request, 'carrito.html', {
        'items': items,
        'total': total
    })

# Asegúrate de que las otras funciones también estén presentes:
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not created:
        item.cantidad += 1
        item.save()
        
    return redirect('inicio')
