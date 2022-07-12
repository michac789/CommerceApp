from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from sso.models import User
from catalog.models import Chat, ChatContent


def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Http404("Invalid username, such profile does not exist!")
    return render(request, "profile/profile.html", {
        "user": user
    })


@login_required(login_url="sso:login")
def chats(request):
    print(Chat.objects.filter(buyer=request.user))
    return render(request, "profile/chats.html", {
        "chats": Chat.objects.filter(buyer=request.user)
    })


def chatcontent(request, chat_id):
    try:
        chatcontents = Chat.retrieve_chats(chat_id)
    except Chat.DoesNotExist:
        return Http404("...")
    return render(request, "profile/chatcontent.html", {
        "chatcontents": chatcontents,
    })
