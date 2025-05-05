from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'nombre', 'apellido', 'tipo_usuario', 'is_staff', 'is_superuser')  # 👈 Se agrega tipo_usuario
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'tipo_usuario')  # 👈 Se agrega tipo_usuario

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Información personal'), {'fields': ('nombre', 'apellido', 'tipo_usuario')}),  # 👈 Se agrega tipo_usuario
        (_('Permisos'), {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        (_('Fechas importantes'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'tipo_usuario', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')}  # 👈 Se agrega tipo_usuario
        ),
    )

    search_fields = ('email', 'nombre')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
