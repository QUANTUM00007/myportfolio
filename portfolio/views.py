from django.shortcuts import render
from .models import Skill, About, Project, SkillCategory

def home_view(request):
    return render(request, 'portfolio/home.html')


def about_view(request):
    about = About.objects.first()
    return render(request, 'portfolio/about.html', {"about": about})


def contact_view(request):
    return render(request, 'portfolio/contact.html')


def skill_view(request):
    categories = SkillCategory.objects.prefetch_related('skills').all()
    return render(request, 'portfolio/skills.html', {"categories": categories})


def project_view(request):
    return render(request, 'portfolio/projects.html')
