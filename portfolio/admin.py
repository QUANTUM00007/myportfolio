from django.contrib import admin
from . models import Skill, SkillCategory, Project,\
     Certificate, Course, Contact, About, ProjectImage


admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(SkillCategory)
admin.site.register(About)
admin.site.register(Course)
admin.site.register(Certificate)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
