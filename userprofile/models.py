from django.db import models
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet, ImproperlyConfigured
from sso.models import User


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1chat", null=True)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2chat", null=True)
    user1_updated = models.BooleanField(default=False)
    user2_updated = models.BooleanField(default=False)
    
    def update_true(self, user):
        if self.user1 == user: self.user1_updated = True
        elif self.user2 == user: self.user2_updated = True
        else: raise Exception('Invalid User!')
        return super(Chat, self).save()
    
    def update_false(self, sender_user):
        if self.user1 == sender_user: self.user2_updated = False
        elif self.user2 == sender_user: self.user1_updated = False
        else: raise Exception('Invalid User!')
        return super(Chat, self).save()

    @classmethod
    def create(self, username1, username2):
        return Chat.objects.create(
            user1 = User.objects.get(username = username1),
            user2 = User.objects.get(username = username2)
        )

    @classmethod
    def retrieve_chats(self, username1, username2, content=True):
        try:
            u1 = User.objects.get(username = username1)
            u2 = User.objects.get(username = username2)
        except User.DoesNotExist:
            raise ObjectDoesNotExist()
        try:
            chat = Chat.objects.get(user1=u1, user2=u2)
        except Chat.DoesNotExist:
            try:
                chat = Chat.objects.get(user1=u2, user2=u1)
            except Chat.DoesNotExist:
                raise EmptyResultSet()
        if content:
            chat_contents = []
            for chat_content in chat.contents.all().order_by("time"):
                chat_contents.append(chat_content.serialize())
            return chat_contents, chat.id
        else: return chat
    
    def save(self, *args, **kwargs):
        if (Chat.objects.filter(user1=self.user1, user2=self.user2).exists() or
            Chat.objects.filter(user1=self.user2, user2=self.user1).exists()):
                raise Exception('No duplicate chat model between any two users!')
        if self.user1 == self.user2:
            raise ImproperlyConfigured("You cannot talk to yourself!")
        return super().save(*args, **kwargs)
    
    def serialize(self, user):
        return {
            "id": self.id,
            "username": (self.user1 if self.user2 == user else self.user2),
        }


class ChatContent(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=256, blank=False, default="")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="contents")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")
    time = models.DateTimeField(auto_now=True)
    
    def serialize(self):
        return {
            "sender": self.sender.username,
            "content": self.content,
            "time": self.time.strftime("%b %d %Y, %I:%M %p"),
            "id": self.id,
        }
