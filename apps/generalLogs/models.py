from django.db import models
import uuid
from apps.users.models import CustomUser  # Importa el modelo CustomUser

class GeneralLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_registro = models.CharField(max_length=20)  # Tipo de registro (e.g., "CREACIÓN", "ACTUALIZACIÓN")
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='registros')
    tabla_relacionada = models.CharField(max_length=20, null=True, blank=True)  # Tabla relacionada con el registro
    id_registro = models.UUIDField(null=True, blank=True)  # ID del registro relacionado
    detalles = models.JSONField(null=True, blank=True)  # Detalles adicionales en formato JSON
    fecha_hora = models.DateTimeField(auto_now_add=True)  # Fecha y hora del registro
    origen = models.CharField(max_length=10, null=True, blank=True)  # Origen del registro (e.g., "API", "ADMIN")

    def __str__(self):
        return f"{self.tipo_registro} - {self.usuario} - {self.fecha_hora}"