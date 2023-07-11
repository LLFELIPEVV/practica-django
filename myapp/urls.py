from django.urls import path
from .views import hello, about, index, projects, tasks, create_task, create_project

urlpatterns = [
    path('', index),
    path('about/', about),
    path('hello/<str:username>', hello),
    path('projects/', projects),
    path('tasks/', tasks),
    path('create_task/', create_task),
    path('create_project', create_project),
]
