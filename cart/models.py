from django.db import models
from myshop.models import Item
from sso.models import User


class ItemUserPair(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta: abstract = True
    
    def serialize(self):
        return {
            "item_id": self.item.id,
            "item_title": self.item.title,
            "item_category": self.item.category.category,
            "item_closed": self.item.closed,
            "seller_username": self.item.seller.username,
        }


class Cart(ItemUserPair):
    def __str__(self):
        return f"<Cart Item: {self.item.id}; User: {self.user}>"
    
    def save(self, *args, **kwargs):
        if self.user == self.item.seller:
            raise Exception("cannot add your own item to cart")
        elif self.item.closed:
            raise Exception("item sale is already closed")
        return super(Cart, self).save(*args, **kwargs)


class Bookmark(ItemUserPair):
    def __str__(self):
        return f"<Bookmark Item {self.item.id} & User {self.user}>"
