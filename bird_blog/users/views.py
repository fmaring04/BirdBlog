from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def login_register(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            form_login = CustomAuthenticationForm(request, data=request.POST)
            form_register = CustomUserCreationForm()
            if form_login.is_valid():
                user = form_login.get_user()
                login(request, user)
                return redirect('home')
        elif 'register' in request.POST:
            form_register = CustomUserCreationForm(request.POST)
            form_login = CustomAuthenticationForm()
            if form_register.is_valid():
                user = form_register.save()
                login(request, user)
                return redirect('home')
    else:
        form_login = CustomAuthenticationForm()
        form_register = CustomUserCreationForm()

    return render(request, 'users/login_register.html', {
        'form_login': form_login,
        'form_register': form_register,
    })

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('home')  # Redirige al usuario a la página de inicio


