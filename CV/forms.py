# forms.py
from django import forms
from .models import CustomUser, Profile, Education, Experience, Skill, Certification


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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'address', 'phone', 'nationality', 'profile_picture']
        labels = {
            'full_name': 'Nombre Completo',
            'address': 'Dirección',
            'phone': 'Teléfono',
            'nationality': 'Nacionalidad',
            'profile_picture': 'Foto de Perfil'
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution_name', 'degree', 'start_date', 'end_date', 'description']
        labels = {
            'institution_name': 'Nombre de la Institución',
            'degree': 'Título Obtenido',
            'start_date': 'Fecha de Inicio',
            'end_date': 'Fecha de Finalización',
            'description': 'Descripción de estudios'
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company_name', 'job_title', 'start_date', 'end_date', 'description']
        labels = {
            'company_name': 'Nombre de la Empresa',
            'job_title': 'Cargo',
            'start_date': 'Fecha de Inicio',
            'end_date': 'Fecha de Finalización',
            'description': 'Descripción del trabajo'
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'level']
        labels = {
            'skill_name': 'Habilidad',
            'level': 'Nivel de habilidad'
        }


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['certification_name', 'organization', 'issue_date', 'expiration_date']
        labels = {
            'certification_name': 'Certificación',
            'organization': 'Organización',
            'issue_date': 'Fecha de Emisión',
            'expiration_date': 'Fecha de Expiración'
        }
