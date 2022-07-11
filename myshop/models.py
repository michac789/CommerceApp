from django.db import models
from sso.models import User
#from catalog.models import ItemOrdered


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=32, blank=False, null=False)
    symbol = models.ImageField(blank=True)
    
    def __str__(self):
        return self.category


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    time_created = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items_sold")
    buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="items_bought", blank=True, null=True, default=None)
    # ordereditem = models.ForeignKey(ItemOrdered, on_delete=models.PROTECT, editable=False)
    
    # class Meta:
    #     order_with_respect_to = 'ordereditem'
        

    def __str__(self):
        return f"<Item ID {self.id}: {self.title}>"
    
    def __repr__(self):
        return f"<Item ID: {self.id}, title: {self.title}, seller: {self.seller}, buyer: {self.buyer}>"
