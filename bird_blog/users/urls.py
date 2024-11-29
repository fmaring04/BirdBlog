from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_register, name='login'), # Vista Login
    path('logout/', views.logout_view, name='logout'),  # Vista Logout
]
