from django.contrib.auth.base_user import BaseUserManager

class CustomUserAdmin(BaseUserManager):
    def create_user(self, correo_electronico, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError("El correo electrónico es obligatorio.")
        email = self.normalize_email(correo_electronico)
        user = self.model(correo_electronico=email, **extra_fields)
        user.set_unusable_password()  # No necesitas password real
        user.save()
        return user

    def create_superuser(self, correo_electronico, password=None, **extra_fields):
        extra_fields.setdefault("es_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(correo_electronico, password, **extra_fields)
