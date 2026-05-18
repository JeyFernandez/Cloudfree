from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Modelo extendido para los perfiles de usuario"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nombre_completo = models.CharField(max_length=150, blank=True, null=True)
    bio = models.TextField(blank=True, null=True, max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuarios"
