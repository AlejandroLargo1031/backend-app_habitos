from django.contrib import admin
from .models import AdminLog

@admin.register(AdminLog)
class AdminLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'administrador', 'usuario_objetivo', 'accion', 'fecha_hora')
    search_fields = ('administrador__correo_electronico', 'usuario_objetivo__correo_electronico', 'accion')
    list_filter = ('accion', 'fecha_hora')