from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='about/')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title
    

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.project.title} - {self.caption}"
    

class Contact(models.Model):
    # Retain this model if needed for future purposes
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/', blank=True)
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    certificate_image = models.ImageField(upload_to='courses/certificates/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)  # Optional: Link to course or certificate

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)
    date_issued = models.DateField()
    pdf = models.FileField(upload_to='certificates/pdf', blank=True, null=True)
    link = models.URLField(blank=True, null=True)  # Optional: Link to certificate

    def __str__(self):
        return self.title
    