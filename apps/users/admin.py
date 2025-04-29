from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'correo_electronico', 'nombre_usuario', 'is_staff', 'is_active')
    search_fields = ('correo_electronico', 'nombre_usuario')
    list_filter = ('is_staff', 'is_active')
    ordering = ('correo_electronico',)
    fieldsets = (
        (None, {'fields': ('correo_electronico', 'password')}),
        ('Información personal', {'fields': ('nombre_usuario', 'correo_verificado', 'notificaciones_habilitadas')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('correo_electronico', 'nombre_usuario', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )