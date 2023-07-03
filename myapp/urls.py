from django.urls import path
from .views import hello, about, index, projects, tasks, project, task

urlpatterns = [
    path('', index),
    path('about/', about),
    path('hello/<str:username>', hello),
    path('projects/', projects),
    path('project/<int:id>', project),
    path('tasks/', tasks),
    path('task/<int:id>', task),
]