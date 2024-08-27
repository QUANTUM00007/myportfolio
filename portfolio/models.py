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
