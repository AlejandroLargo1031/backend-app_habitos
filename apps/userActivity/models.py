from django.db import models
import uuid
from apps.users.models import CustomUser  

class UserActivity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='actividades')
    tipo_actividad = models.CharField(max_length=20)
    direccion_ip = models.GenericIPAddressField(null=True, blank=True)
    info_dispositivo = models.JSONField(null=True, blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)