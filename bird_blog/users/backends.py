from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Intentar autenticar por correo
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # Si no se encuentra, intentar autenticar por nombre de usuario
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        # Verificar contraseña
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
