from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile

class RegistroForm(UserCreationForm):
    """Formulario mejorado para el registro de usuarios"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'correo@ejemplo.com'
        })
    )
    nombre_completo = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Tu nombre completo'
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "nombre_completo", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Estilos Tailwind responsivos para los campos
        input_classes = 'w-full bg-slate-900 border border-slate-800 rounded-lg sm:rounded-xl p-2 sm:p-3 text-white text-sm sm:text-base focus:border-blue-500 outline-none transition-all'
        
        self.fields['username'].widget.attrs.update({
            'class': input_classes,
            'placeholder': 'nombre_de_usuario'
        })
        self.fields['password1'].widget.attrs.update({
            'class': input_classes,
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': input_classes,
            'placeholder': 'Confirmar contraseña'
        })
        
        for field_name in ['email', 'nombre_completo']:
            self.fields[field_name].widget.attrs.update({
                'class': input_classes
            })

    def clean_email(self):
        """Validar que el email no esté registrado"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email

    def clean_username(self):
        """Validar que el username tenga al menos 3 caracteres"""
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("El nombre de usuario debe tener al menos 3 caracteres.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Crear o actualizar el perfil del usuario
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.nombre_completo = self.cleaned_data['nombre_completo']
            profile.save()
        return user


class EditarPerfilForm(forms.ModelForm):
    """Formulario para editar el perfil del usuario"""
    class Meta:
        model = UserProfile
        fields = ('nombre_completo', 'bio')
        input_classes = 'w-full bg-slate-900 border border-slate-800 rounded-lg sm:rounded-xl p-2 sm:p-3 text-white text-sm sm:text-base focus:border-blue-500 outline-none transition-all'
        widgets = {
            'nombre_completo': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900 border border-slate-800 rounded-lg sm:rounded-xl p-2 sm:p-3 text-white text-sm sm:text-base focus:border-blue-500 outline-none transition-all',
                'placeholder': 'Tu nombre completo'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'w-full bg-slate-900 border border-slate-800 rounded-lg sm:rounded-xl p-2 sm:p-3 text-white text-sm sm:text-base focus:border-blue-500 outline-none transition-all',
                'placeholder': 'Cuéntanos sobre ti (máx. 500 caracteres)',
                'rows': 4
            }),
        }


class CambiarContraseñaForm(forms.Form):
    """Formulario para cambiar la contraseña"""
    input_classes = 'w-full bg-slate-900 border border-slate-800 rounded-lg sm:rounded-xl p-2 sm:p-3 text-white text-sm sm:text-base focus:border-blue-500 outline-none transition-all'
    
    contraseña_actual = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full bg-slate-900 border border-slate-800 rounded-lg sm:rounded-xl p-2 sm:p-3 text-white text-sm sm:text-base focus:border-blue-500 outline-none transition-all',
            'placeholder': 'Contraseña actual'
        })
    )
    contraseña_nueva = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full bg-slate-900 border border-slate-800 rounded-lg sm:rounded-xl p-2 sm:p-3 text-white text-sm sm:text-base focus:border-blue-500 outline-none transition-all',
            'placeholder': 'Nueva contraseña'
        })
    )
    confirmar_contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full bg-slate-900 border border-slate-800 rounded-lg sm:rounded-xl p-2 sm:p-3 text-white text-sm sm:text-base focus:border-blue-500 outline-none transition-all',
            'placeholder': 'Confirmar nueva contraseña'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        nueva = cleaned_data.get('contraseña_nueva')
        confirmar = cleaned_data.get('confirmar_contraseña')
        
        if nueva and confirmar and nueva != confirmar:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        if nueva and len(nueva) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        
        return cleaned_data