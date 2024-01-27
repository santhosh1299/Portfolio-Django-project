from django.shortcuts import render
from .models import Project
def home(request):
    projects = Project.objects.all()
    return (render(request,'portfolio/home.html',{'projects':projects}))
def ml_project(request):
    return (render(request,'portfolio/ml_project.html'))