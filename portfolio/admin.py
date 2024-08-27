from django.contrib import admin
from . models import Skill, SkillCategory, Project, Contact, About


admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(SkillCategory)
admin.site.register(About)
