from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    return HttpResponse("<h1>Bienvenido</h1>")

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request, id):
    return HttpResponse("<h2>About %s</h2>" %id)

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def project(request, id):
    project = get_object_or_404(Project, id=id)
    return HttpResponse("Project: %s" % project.name)

def tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe=False)

def task(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse("task: %s" % task.title)