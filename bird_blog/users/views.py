from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def login_register(request):
    if request.method == 'POST':
        if 'login' in request.POST:  # Si es una solicitud de login
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')  # Redirige al home si el login es exitoso
        elif 'register' in request.POST:  # Si es una solicitud de registro
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)  # Inicia sesión automáticamente al registrar
                return redirect('home')
    else:
        form_login = AuthenticationForm()
        form_register = UserCreationForm()

    return render(request, 'users/login_register.html', {
        'form_login': form_login,
        'form_register': form_register
    })


