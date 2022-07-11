from django.contrib import admin
from .models import Chat, ChatContent, ItemOrdered


admin.site.register(Chat)
admin.site.register(ChatContent)
admin.site.register(ItemOrdered)
