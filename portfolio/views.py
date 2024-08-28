from django.shortcuts import render, get_object_or_404
from .models import Skill, About, Project, SkillCategory, Course, Certificate

def home_view(request):
    projects = Project.objects.all()
    courses = Course.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/home.html', 
                    {"projects": projects, "courses": courses, "certificates": certificates})


def about_view(request):
    about = About.objects.first()
    return render(request, 'portfolio/about.html', {"about": about})


def contact_view(request):
    return render(request, 'portfolio/contact.html')


def skill_view(request):
    categories = SkillCategory.objects.prefetch_related('skills').all()
    return render(request, 'portfolio/skills.html', {"categories": categories})


# def project_view(request):
#     projects = Project.objects.all()
#     return render(request, 'portfolio/projects.html', {'projects': projects})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    images = project.images.all()  # Retrieve all images related to the project
    return render(request, 'portfolio/project_detail.html', {'project': project, 'images': images})
