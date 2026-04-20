from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
from django.db import models
from django.conf import settings
from productos.models import Producto # Asegúrate de importar tus productos

User = settings.AUTH_USER_MODEL

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

# Tu clase Pedido se queda igual abajo...

    # ... (el código que ya tienes)

class Pedido(models.Model):

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado por vendedor'),
        ('rechazado', 'Rechazado'),
        ('preparado', 'Preparado por bodega'),
        ('enviado', 'Enviado'),
        ('pagado', 'Pago confirmado'),
        ('entregado', 'Entregado'),
    ]

    METODOS_PAGO = [
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
        ('transferencia', 'Transferencia'),
    ]

    TIPOS_ENTREGA = [
        ('retiro', 'Retiro en tienda'),
        ('despacho', 'Despacho a domicilio'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=30, choices=ESTADOS, default='pendiente')
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    tipo_entrega = models.CharField(max_length=20, choices=TIPOS_ENTREGA)
    fecha = models.DateTimeField(auto_now_add=True)