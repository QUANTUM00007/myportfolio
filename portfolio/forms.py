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

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
#         'placeholder': 'Your Name'
#     }))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={
#         'placeholder': 'Your Email'
#     }))
#     message = forms.CharField(widget=forms.Textarea(attrs={
#         'placeholder': 'Your Message'
#     }))


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message') 