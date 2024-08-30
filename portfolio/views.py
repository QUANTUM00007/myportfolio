from django.shortcuts import render, redirect, get_object_or_404
from .models import Skill, About, Project, SkillCategory, Course, Certificate
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .utils import send_telegram_message  # Import the function


def home_view(request):
    projects = Project.objects.all()
    courses = Course.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/home.html', 
                    {"projects": projects, "courses": courses, "certificates": certificates})


def about_view(request):
    about = About.objects.first()
    return render(request, 'portfolio/about.html', {"about": about})


# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Attempt to send the email and handle any exceptions
#             try:
#                 send_mail(
#                     f'Contact Form Submission from {name}',
#                     message,
#                     email,
#                     ['mohdarslan626@gmail.com'],
#                     fail_silently=False,
#                 )
#                 messages.success(request, 'Thank you for your message. We will get back to you soon!')
#             except Exception as e:
#                 messages.error(request, f'An error occurred while sending the message: {e}')
#                 return redirect('contact')
            
#             return redirect('contact')
#     else:
#         form = ContactForm()

#     return render(request, 'portfolio/contact.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_telegram_message(name, email, message)
                messages.success(request, 'Thank you for your message. We will get back to you soon!')
            except Exception as e:
                messages.error(request, f'An error occurred while sending the message: {e}')
                return redirect('contact')

            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})


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
