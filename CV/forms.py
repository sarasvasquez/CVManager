# forms.py
from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = User
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
