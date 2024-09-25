from django.shortcuts import render, redirect
from .forms import ProfileForm, EducationForm, WorkExperienceForm, SkillForm, ProjectForm

def create_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        education_form = EducationForm(request.POST)
        work_experience_form = WorkExperienceForm(request.POST)
        skill_form = SkillForm(request.POST)
        project_form = ProjectForm(request.POST)
        
        if (profile_form.is_valid() and education_form.is_valid() and 
            work_experience_form.is_valid() and skill_form.is_valid() and 
            project_form.is_valid()):
            
            profile = profile_form.save(commit=False)
            profile.user = request.user  # Asignamos el usuario actual al perfil
            profile.save()
            
            # Guardar las otras partes
            education_form.save(commit=False).profile = profile
            education_form.save()

            work_experience_form.save(commit=False).profile = profile
            work_experience_form.save()

            skill_form.save(commit=False).profile = profile
            skill_form.save()

            project_form.save(commit=False).profile = profile
            project_form.save()

            return redirect('profile_success')  # Redirige a una página de éxito

    else:
        profile_form = ProfileForm()
        education_form = EducationForm()
        work_experience_form = WorkExperienceForm()
        skill_form = SkillForm()
        project_form = ProjectForm()

    return render(request, 'create_profile.html', {
        'profile_form': profile_form,
        'education_form': education_form,
        'work_experience_form': work_experience_form,
        'skill_form': skill_form,
        'project_form': project_form,
    })

