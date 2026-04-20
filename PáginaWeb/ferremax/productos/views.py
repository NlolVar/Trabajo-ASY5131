from django.shortcuts import render
from .models import Producto

def inicio(request):
    # Traemos todos los productos de la DB
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})
