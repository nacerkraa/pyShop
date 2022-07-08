from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def add(request):
    return HttpResponse("Add a new product")