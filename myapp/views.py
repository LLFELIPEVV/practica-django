from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    return render(request, "index.html")

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
    return render(request, "about.html")

def projects(request):
    projects = list(Project.objects.values())
    return render(request, "projects.html")

def project(request, id):
    project = get_object_or_404(Project, id=id)
    return HttpResponse("Project: %s" % project.name)

def tasks(request):
    tasks = list(Task.objects.values())
    return render(request, "tasks.html")

def task(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse("task: %s" % task.title)