from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from usuarios.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework import serializers, generics
from .serializers import UsuarioSerializer
from rest_framework import viewsets
from .models import CustomUser
from .serializers import UsuarioSerializer

# Serializador personalizado para login con email
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = CustomUser.EMAIL_FIELD

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if not user:
            raise serializers.ValidationError('Credenciales inválidas')

        data = super().validate(attrs)
        return data

# Vista personalizada para login
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Vista para registro de usuario (solo clientes)
class RegistroUsuarioAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerializer
