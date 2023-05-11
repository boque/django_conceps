from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Projects, Task

# Create your views here.

def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title':title
    })
    

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
    return render(request, 'about.html')


def projects(request):
    projects = Projects.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks': tasks
    })