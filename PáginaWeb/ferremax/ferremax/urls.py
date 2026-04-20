from django.contrib import admin
from django.urls import path
from productos import views as prod
from pedidos import views as ped
from accounts import views as acc # <--- Asegúrate de que esta línea esté

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal
    path('', prod.inicio, name='inicio'),

    # Carrito
    path('carrito/', ped.ver_carrito, name='carrito'),
    path('agregar/<int:producto_id>/', ped.agregar_al_carrito, name='agregar_al_carrito'),

    # Autenticación (LAS QUE FALTABAN)
    path('login/', acc.login_view, name='login'),
    path('registro/', acc.registro, name='registro'),
    path('logout/', acc.logout_view, name='logout'),
]
