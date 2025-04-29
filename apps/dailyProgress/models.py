from django.db import models
import uuid
from apps.habits.models import Habit  # Importa Habit desde apps.habits.models

class DailyProgress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    habito = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='progresos')
    fecha = models.DateField()
    completado = models.BooleanField(default=False)
    cantidad = models.IntegerField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('habito', 'fecha')