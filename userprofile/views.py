from django.views.generic.base import TemplateView
from django.views import View
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet, ImproperlyConfigured
from django.http import HttpResponseBadRequest, JsonResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from json import loads
from time import sleep

from .decorator import api_view
from sso.models import User
from .models import Chat, ChatContent
from commerceapp.settings import LOGIN_URL


class ProfileView(TemplateView):
    template_name = "profile/profile.html"
    
    def get_context_data(self, **kwargs):
        return {"user": get_object_or_404(User, username = kwargs["username"])}


@method_decorator([login_required(login_url=LOGIN_URL)], name="dispatch")
class AllChat(TemplateView):
    template_name = "profile/allchat.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chats"] = []
        for chat in Chat.objects.filter(Q(user1=self.request.user) |
                                        Q(user2=self.request.user)):
            context["chats"].append(chat.serialize(self.request.user))
        return context


@method_decorator([login_required(login_url=LOGIN_URL)], name="dispatch")
class ViewChat(View):
    def get(self, request, username):
        if request.user.username == username:
            return HttpResponseBadRequest("You cannot talk to yourself!")
        return render(request, "profile/chatview.html", {
            "username": username,
        })


@method_decorator([csrf_exempt, api_view("GET", "POST", "PATCH"),
                   login_required], name="dispatch")
class FetchChat(View):
    def get(self, request, username):
        try:
            chat, id = Chat.retrieve_chats(request.user.username, username)
        except ObjectDoesNotExist:
            return JsonResponse({ "error": "Invalid username!",}, status=400)
        except EmptyResultSet:
            Chat.create(request.user.username, username)
            chat, id = Chat.retrieve_chats(request.user.username, username)
        except ImproperlyConfigured:
            return JsonResponse({ "error": "Cannot chat to yourself!",}, status=400)
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
