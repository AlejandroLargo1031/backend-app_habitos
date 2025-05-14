from datetime import date, datetime
import uuid
from django.db import models
from django.conf import settings
from apps.users.models import CustomUser

class Habito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, null=True, blank=True)
    tipo_habito = models.CharField(max_length=20, null=True, blank=True)
    objetivo = models.IntegerField(default=1)  # Cambiado de null a default 1
    meta_unidad = models.CharField(max_length=20, null=True, blank=True)
    frecuencia = models.CharField(max_length=20, default="diario")  # Valor por defecto
    racha_actual = models.IntegerField(default=0)
    racha_record = models.IntegerField(default=0)  # Eliminada la propiedad que lo anulaba
    color = models.CharField(max_length=7, default="#FFFFFF")
    creado_en = models.DateTimeField(auto_now_add=True)
    actual = models.IntegerField(default=0)
    icono = models.CharField(max_length=20, null=True, blank=True)
    completed_dates = models.JSONField(default=list, blank=True)
    last_reset = models.DateField(auto_now=True)  # Cambiado de default=date.today

    class Meta:
        db_table = "habitos"
        verbose_name = "Hábito"
        verbose_name_plural = "Hábitos"

    def __str__(self):
        return f"{self.nombre} - {self.usuario.email}"
    
    def update_streaks(self):
        """Actualiza automáticamente las rachas basado en completed_dates"""
        if not self.completed_dates:
            self.racha_actual = 0
            return

        try:
            dates = sorted(
                [datetime.strptime(d, '%Y-%m-%d').date() 
                 for d in self.completed_dates
            ])
            
            current_streak = 1
            max_streak = 1

            for i in range(1, len(dates)):
                if (dates[i] - dates[i-1]).days == 1:
                    current_streak += 1
                    max_streak = max(max_streak, current_streak)
                else:
                    current_streak = 1

            self.racha_actual = current_streak
            self.racha_record = max(max_streak, self.racha_record)

        except Exception as e:
            print(f"Error calculando rachas: {str(e)}")

