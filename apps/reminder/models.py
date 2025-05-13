from django.db import models
import uuid
from apps.habito.models import Habito

class Reminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    habito = models.ForeignKey(Habito, on_delete=models.CASCADE, related_name='recordatorios')
    horarios = models.JSONField()  # Almacena los horarios de los recordatorios en formato JSON
    silenciar_desde = models.TimeField(null=True, blank=True)  # Hora de inicio para silenciar recordatorios
    silenciar_hasta = models.TimeField(null=True, blank=True)  # Hora de fin para silenciar recordatorios
    creado_en = models.DateTimeField(auto_now_add=True)  # Fecha de creación del recordatorio

    def __str__(self):
        return f"Recordatorio para el hábito: {self.habito.nombre}"