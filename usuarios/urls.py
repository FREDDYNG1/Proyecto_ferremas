from django.urls import path
from .views import CustomTokenObtainPairView, RegistroUsuarioAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('registro/', RegistroUsuarioAPIView.as_view(), name='registro'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
