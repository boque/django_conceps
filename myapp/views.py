from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Projects, Task

# Create your views here.

def index(request):
    return HttpResponse("<h2>index page </h2>")
    

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
    return HttpResponse("<h2>About </h2>")


def projects(request):
    projects = list(Projects.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    tasks = get_object_or_404(Task, id=id)
    return HttpResponse("tasks: %s"  %tasks.title )