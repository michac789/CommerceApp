from django.shortcuts import render
from django.http import Http404

from sso.models import User


def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Http404("Invalid username, such profile does not exist!")
    return render(request, "profile/profile.html", {
        "user": user
    })