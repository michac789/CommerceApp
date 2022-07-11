from django.db import models
from myshop.models import Item
from sso.models import User


class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="oncart")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="oncart")
    
    def __str__(self):
        return f"<Item: {self.item}; User: {self.user}>"
