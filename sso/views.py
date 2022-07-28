from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.db import IntegrityError

from .models import User, AdminPost


def register_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        
        # username or email cannot be empty
        if not username or not email:
            return render(request, "sso/register.html", {
                "error": "Error! This Please fill all the required fields!",
                "username": username, "email": email,
            })
        
        # password must match confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "sso/register.html", {
                "error": "Error! Confirmation password does not match original password!",
                "username": username, "email": email,
            })
            
        # username must be unique
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "sso/register.html", {
                "error": "Error! Username has been taken, please choose another username!",
                "username": username, "email": email,
            })
            
        # ensure password is not too simple
        try:
            validate_password(password)
        except ValidationError:
            return render(request, "sso/register.html", {
                "error": "Error! Password too simple, please pick a stronger password!",
                "username": username, "email": email,
            })
            
        # log user in and redirect to catalog main page
        login(request, user)
        return HttpResponseRedirect(reverse("catalog:index"))
    else:
        # redirect to catalog main page if user has already logged in
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("catalog:index"))
        
        # if not render register page normally
        return render(request, "sso/register.html", {
            "error": "", "username": "", "email": "",
        })


def login_view(request):
    # attempt to sign user in and check if authentication successful
    if request.method == "POST":
        user = authenticate(request,
                            username = request.POST["username"],
                            password = request.POST["password"])
        
        # log the user in and redirect to catalog main page if successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("catalog:index"))
        
        # otherwise display an error message
        else: return render(request, "sso/login.html", {
            "error": "Error! Invalid username and/or password!"
        })
    else:
        # if user already logged in, redirect to catalog main page
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("catalog:index"))
        
        # if not render login form
        return render(request, "sso/login.html")


def logout_view(request):
    # log the user out and renders logout page
    logout(request)
    return render(request, "sso/logout.html")


def tc(request):
    # render terms and conditions page
    return render(request, "sso/t&c.html", {
        "post": AdminPost.objects.get(id=1).serialize()
    })
