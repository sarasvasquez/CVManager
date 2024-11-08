# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import *


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Usamos la contraseña creada por el usuario
            user.save()
            login(request, user)  # Inicia sesión después del registro
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {user.username}!')
                return redirect('home')  # Redirige a la página de inicio o a otra página de tu elección
            else:
                messages.error(request, 'Credenciales inválidas, inténtalo nuevamente.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


