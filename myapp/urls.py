from django.urls import path
from .views import hello, about, index, projects, tasks, create_task, create_project

urlpatterns = [
    path('', index, name = "index"),
    path('about/', about, name = "about"),
    path('hello/<str:username>', hello, name = "hello"),
    path('projects/', projects, name = "projects"),
    path('tasks/', tasks, name = "tasks"),
    path('create_task/', create_task, name = "create_task"),
    path('create_project/', create_project, name = "create_project"),
]
