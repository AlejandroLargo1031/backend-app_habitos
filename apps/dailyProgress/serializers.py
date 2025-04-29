from rest_framework import serializers
from .models import DailyProgress

class DailyProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyProgress
        fields = '__all__'
        read_only_fields = ('creado_en',)