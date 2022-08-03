from django.views.generic.base import TemplateView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from json import loads
from time import sleep

from sso.models import User
from .models import Chat, ChatContent


class ProfileView(TemplateView):
    template_name = "profile/profile.html"
    
    def get_context_data(self, **kwargs):
        return {"user": get_object_or_404(User, username = kwargs["username"])}


class ViewChat(TemplateView):
    template_name = "profile/chatview.html"


@method_decorator([csrf_exempt], name="dispatch")
class FetchChat(View):
    def get(self, request, username):
        try:
            chat, id = Chat.retrieve_chats(request.user.username, username)
        except ObjectDoesNotExist:
            return JsonResponse({ "error": "Invalid username!",}, status=400)
        except EmptyResultSet:
            Chat.create(request.user.username, username)
            chat, id = Chat.retrieve_chats(request.user.username, username)
        tmpchat = Chat.objects.get(id=id)
        tmpchat.update_true(request.user)
        return JsonResponse({ "chat": chat, "id": id,})

    def post(self, request, username):
        data = loads(request.body)
        chat = Chat.retrieve_chats(request.user.username, username, False)
        newchat = ChatContent.objects.create(
            content = data["content"], chat = chat, sender = request.user,
        )
        chat.update_false(request.user)
        return JsonResponse({ "success": "chat sent", "new": newchat.serialize(),})
    
    def patch(self, request, username):
        for _ in range(300):
            chat = Chat.retrieve_chats(request.user.username, username, False)
            if chat.user1 == request.user: x = chat.user1_updated
            elif chat.user2 == request.user: x = chat.user2_updated
            if x == False: break
            sleep(0.2)
        return JsonResponse({ "up_to_date": x,})


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
