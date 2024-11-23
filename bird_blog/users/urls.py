from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login_register/', views.login_register, name='login_register'),
]
