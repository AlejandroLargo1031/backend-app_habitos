import uuid 
from django.db import models
from apps.habito.models import Habito  # Asegúrate de que la importación sea correcta

class DailyProgress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Recomendado para UUID
    habito = models.ForeignKey(
        Habito, 
        on_delete=models.CASCADE,  # Elimina registros DailyProgress cuando se borre el Hábito
        related_name="daily_progress"
    )
    fecha = models.DateField()
    completado = models.BooleanField(default=False)

    class Meta:
        db_table = "daily_progress"  # Opcional: nombre personalizado para la tabla
        verbose_name_plural = "Daily Progress"  # Nombre legible en el admin

    def __str__(self):
        return f"{self.habito.nombre} - {self.fecha}"