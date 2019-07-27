from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):

    return render(request, "index.html")

def login(request):
    
    return render(request, "login.html")

def signup(request):
    
    return render(request, "signup.html")

