from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('skills/', views.skill_view, name='skills'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('projects/', views.project_view, name='projects'),
]