from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Función de Registro que te faltaba
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Inicia sesión automáticamente al registrarse
            messages.success(request, "¡Registro exitoso! Bienvenido a FERREMAS.")
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

# Asegúrate de tener también estas para que no den error después
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('inicio')
