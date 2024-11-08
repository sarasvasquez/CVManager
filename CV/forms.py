# forms.py
from django import forms
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = CustomUser
        fields = ['email', 'username']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

class ProfileForm(forms.Form):
    # Sección de Datos Personales
    full_name = forms.CharField(max_length=255, required=True, label="Nombre Completo")
    address = forms.CharField(max_length=255, required=True, label="Dirección")
    phone = forms.CharField(max_length=20, required=True, label="Teléfono")
    nationality = forms.CharField(max_length=100, required=True, label="Nacionalidad")
    profile_picture = forms.ImageField(required=False, label="Foto de Perfil")

    # Sección de Educación
    institution_name = forms.CharField(max_length=255, required=True, label="Nombre de la Institución")
    degree = forms.CharField(max_length=255, required=True, label="Título Obtenido")
    start_date_education = forms.DateField(required=True, label="Fecha de Inicio")
    end_date_education = forms.DateField(required=True, label="Fecha de Finalización")
    description_education = forms.CharField(widget=forms.Textarea, required=False, label="Descripción de estudios")

    # Sección de Experiencia
    company_name = forms.CharField(max_length=255, required=True, label="Nombre de la Empresa")
    job_title = forms.CharField(max_length=255, required=True, label="Cargo")
    start_date_experience = forms.DateField(required=True, label="Fecha de Inicio")
    end_date_experience = forms.DateField(required=True, label="Fecha de Finalización")
    description_experience = forms.CharField(widget=forms.Textarea, required=False, label="Descripción del trabajo")

    # Sección de Habilidades
    skill_name = forms.CharField(max_length=100, required=True, label="Habilidad")
    level = forms.CharField(max_length=100, required=True, label="Nivel de habilidad")

    # Sección de Certificaciones
    certification_file = forms.FileField(required=False, label="Certificaciones")