from rest_framework import serializers
from .models import CustomUser

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'nombre', 'apellido', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['tipo_usuario'] = 'cliente'  # 🔒 fuerza cliente por API
        return CustomUser.objects.create_user(**validated_data)
