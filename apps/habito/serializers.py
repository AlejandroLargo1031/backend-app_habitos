from datetime import datetime
from rest_framework import serializers
from .models import Habito

class HabitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habito
        fields = '__all__'
        read_only_fields = ('usuario', 'creado_en', 'id', 'last_reset')
        extra_kwargs = {
            'nombre': {'required': False},  
            'objetivo': {'required': False}  
        }
    
    