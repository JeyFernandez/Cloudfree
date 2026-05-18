from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('perfil/editar/', views.editar_perfil_view, name='editar_perfil'),
    path('perfil/cambiar-contraseña/', views.cambiar_contraseña_view, name='cambiar_contraseña'),
    path('logout/', views.logout_view, name='logout'),
]
