from django.db import models
import uuid
from apps.users.models import CustomUser

class Habit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='habitos')
    nombre = models.CharField(max_length=20)
    categoria = models.CharField(max_length=12, null=True, blank=True)
    tipo_habito = models.CharField(max_length=12, null=True, blank=True)
    objetivo = models.IntegerField()
    racha_actual = models.IntegerField(default=0)
    racha_maxima = models.IntegerField(default=0)
    color = models.CharField(max_length=7, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre