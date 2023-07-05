from django.urls import path
from .views import hello, about, index, projects, tasks

urlpatterns = [
    path('', index),
    path('about/', about),
    path('hello/<str:username>', hello),
    path('projects/', projects),
    path('tasks/', tasks),
]