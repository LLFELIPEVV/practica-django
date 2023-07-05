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

def tasks(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, "tasks.html", {'tasks': tasks})