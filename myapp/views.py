from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Projects, Task

# Create your views here.

def index(request):
    return render(request, 'index.html')
    

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
    return render(request, 'about.html')


def projects(request):
    projects = list(Projects.objects.values())
    return render(request, 'projects.html')

def tasks(request):
    #tasks = get_object_or_404(Task, id=id)
    return render(request, 'task.html')