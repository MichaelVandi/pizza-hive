from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        # Return the index page
        return render(request, "index.html")
    context ={
        "user": request.user
    }
    return HttpResponseRedirect(reverse("shopping"))

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {"message": "Invalid credentials."})
    return render(request, "login.html", {"message": ""})

def logout_view(request):
    logout(request)
    return render(request, "index.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password= request.POST["password"]
        confirm= request.POST["confirm"]
        first_name= request.POST["firstname"]
        last_name= request.POST["lastname"]
        email= request.POST["email"]
        # Check if all fields are filled
        if username == '' or password == '' or confirm == '' or first_name == '' \
            or last_name == '' or email == '':
            # One or more fields are empty show message
            return render(request, "signup.html", {"message": "One or more fields empty"})
        if password != confirm:
            # Passwords don match show message
            return render(request, "signup.html", {"message": "Passwords do not match"})
        
        # Conditions met, add new user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password = password,
            )
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            # New user created redirect user to login page
            return render(request, "login.html", {"new_user_msg": "Welcome "+ first_name + " you can now log in"} )
        except IntegrityError:
            # User already exists
            return render(request, "signup.html", {"message": "User already exist"})


    return render(request, "signup.html")

