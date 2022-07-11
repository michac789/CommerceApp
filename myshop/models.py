from django.db import models
from sso.models import User


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=32, blank=False, null=False)
    symbol = models.ImageField(blank=True)
    
    def __str__(self):
        return self.category


class ItemManager(models.Manager):
    def __init__(self, **kwargs):
        self.sold = kwargs["sold"]
        super().__init__()

    def get_queryset(self):
        if self.sold:
            return super().get_queryset().exclude(buyer=None)
        else:
            return super().get_queryset().filter(buyer=None, closed=False)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    image = models.CharField(max_length=128, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    time_created = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items_sold")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items_bought", blank=True, null=True, default=None)
    ordereditem = models.ForeignKey("catalog.ItemOrdered", on_delete=models.PROTECT, editable=False, blank=True, null=True)
    closed = models.BooleanField(default=False)
    
    objects = models.Manager()
    sold = ItemManager(sold=True)
    onsale = ItemManager(sold=False)
    
    class Meta:
        order_with_respect_to = 'ordereditem'
        
    def __str__(self):
        return f"<Item ID {self.id}: {self.title}>"
    
    def __repr__(self):
        return f"<Item ID: {self.id}, title: {self.title}, seller: {self.seller}, buyer: {self.buyer}>"
    
    def getstatus(self, user):
        return {
            "creator": self.seller == user,
            "sold": self.buyer != None,
        }
        
    def formhandler(self):
        return {
            'title': self.title,
            'description': self.description,
            'image': self.image,
            "price": self.price,
            "category": self.category,
        }
