from django import forms
from .models import Project, ProjectImage

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']  # Add other fields as necessary

class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image', 'caption']
