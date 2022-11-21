from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Image, Project
from .forms import ProjectForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
    form = ProjectForm()

    return render(request, 'project_form.html', {'form': form})

def upload_images(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'upload.html', context)

def home(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)

def file_upload(request):
    if request.method == 'POST':
        project = request.POST.get('project')
        pictures = request.FILES.get('file')
        Image.objects.create(project_id=project, picture=pictures)
        return redirect('/')
    
