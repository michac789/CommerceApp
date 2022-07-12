from django.db import models
from sso.models import User
from myshop.models import Item


# class ChatManager(models.Manager):
#     def retrieve_chat(self):
#         return "TODO"
    
#     def getchats_user(self, user_id):
#         return self.filter(buyer=user_id)


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="chat")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer_chat")
    
    # objects = ChatManager()
    
    @classmethod
    def retrieve_chats(self, id):
        return Chat.objects.get(id=id).contents.all().order_by("time")


class ChatContent(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=256, blank=False, default="")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="contents")
    time = models.DateTimeField(auto_now=True)


class ItemOrdered(models.Model):
    id = models.AutoField(primary_key=True)
