from django.db import models
import uuid
from apps.users.models import CustomUser  

class AdminLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    administrador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='registros_administrador')
    usuario_objetivo = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='registros_objetivo')
    accion = models.CharField(max_length=50)  
    detalles = models.JSONField(null=True, blank=True) 
    fecha_hora = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.administrador} realizó {self.accion} sobre {self.usuario_objetivo} el {self.fecha_hora}"