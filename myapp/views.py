from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>index page </h2>")
    

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" %username)

def about(request):
    return HttpResponse("<h2>About </h2>")