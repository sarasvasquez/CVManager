# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ProfileForm, EducationForm, ExperienceForm, SkillForm, CertificationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Usamos la contraseña creada por el usuario
            user.save()
            login(request, user)  # Inicia sesión después del registro
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {user.username}!')
                return redirect('home')  # Redirige a la página de inicio o a otra página de tu elección
            else:
                messages.error(request, 'Credenciales inválidas, inténtalo nuevamente.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    # Get or create profile for the user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        education_form = EducationForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        skill_form = SkillForm(request.POST)
        certification_form = CertificationForm(request.POST)

        if profile_form.is_valid():
            profile_form.save()

            # Save additional information if each form is valid
            if education_form.is_valid():
                education = education_form.save(commit=False)
                education.profile = profile
                education.save()

            if experience_form.is_valid():
                experience = experience_form.save(commit=False)
                experience.profile = profile
                experience.save()

            if skill_form.is_valid():
                skill = skill_form.save(commit=False)
                skill.profile = profile
                skill.save()

            if certification_form.is_valid():
                certification = certification_form.save(commit=False)
                certification.profile = profile
                certification.save()

            messages.success(request, "El formulario se ha guardado correctamente.")
            return redirect('view_profile')
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        profile_form = ProfileForm(instance=profile)
        education_form = EducationForm()
        experience_form = ExperienceForm()
        skill_form = SkillForm()
        certification_form = CertificationForm()

    return render(request, 'profile.html', {
        'profile_form': profile_form,
        'education_form': education_form,
        'experience_form': experience_form,
        'skill_form': skill_form,
        'certification_form': certification_form,
    })

@login_required(login_url='login')  # Ensures only authenticated users can access this view
def view_profile(request):
    # Fetch the current user's profile
    profile = get_object_or_404(Profile, user=request.user)

    # Render the 'view_profile.html' template with profile data
    return render(request, 'view_profile.html', {'profile': profile})
