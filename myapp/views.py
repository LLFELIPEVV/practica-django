from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, "index.html", {'title': title})

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
    username = 'felipe'
    return render(request, "about.html", {'username': username})

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects.html", {'projects': projects})

def project(request, id):
    project = get_object_or_404(Project, id=id)
    return HttpResponse("Project: %s" % project.name)

def tasks(request):
    tasks = list(Task.objects.values())
    return render(request, "tasks.html")

def task(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse("task: %s" % task.title)