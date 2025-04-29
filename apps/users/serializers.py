from rest_framework import serializers
from apps.users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'correo_electronico', 'nombre_usuario', 'is_active', 'is_staff']
        read_only_fields = ['id', 'is_active', 'is_staff']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['correo_electronico', 'nombre_usuario', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            correo_electronico=validated_data['correo_electronico'],
            nombre_usuario=validated_data['nombre_usuario'],
            password=validated_data['password']
        )
        return user