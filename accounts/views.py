from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction
from .forms import RegistroForm, EditarPerfilForm, CambiarContraseñaForm
from .models import UserProfile

def registro_view(request):
    """Vista para registrar nuevos usuarios"""
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'¡Bienvenido {user.username}! Tu cuenta ha sido creada exitosamente.')
            login(request, user)
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegistroForm()
    
    return render(request, 'registration/registro.html', {'form': form})


@login_required
def perfil_view(request):
    """Vista del perfil del usuario autenticado"""
    profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'profile_user': request.user,
        'profile': profile,
    }
    return render(request, 'registration/perfil.html', context)


@login_required
def editar_perfil_view(request):
    """Vista para editar el perfil del usuario"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('accounts:perfil')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = EditarPerfilForm(instance=profile)
    
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'registration/editar_perfil.html', context)


@login_required
def cambiar_contraseña_view(request):
    """Vista para cambiar la contraseña"""
    if request.method == 'POST':
        form = CambiarContraseñaForm(request.POST)
        if form.is_valid():
            user = request.user
            contraseña_actual = form.cleaned_data['contraseña_actual']
            
            if not user.check_password(contraseña_actual):
                messages.error(request, 'La contraseña actual es incorrecta.')
            else:
                contraseña_nueva = form.cleaned_data['contraseña_nueva']
                user.set_password(contraseña_nueva)
                user.save()
                messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
                return redirect('accounts:perfil')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = CambiarContraseñaForm()
    
    context = {'form': form}
    return render(request, 'registration/cambiar_contraseña.html', context)


@login_required
def logout_view(request):
    """Vista para cerrar sesión"""
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('/')