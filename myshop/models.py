from django.db import models
from sso.models import User
from django.core.serializers import serialize
from json import loads


class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller")
    location = models.CharField(max_length=128)
    joined_time = models.DateTimeField(auto_now=True)
    # other fields - TODO
    
    def __str__(self) -> str:
        return f"<seller: {self.user.username}>"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=32, blank=False, null=False)
    code = models.CharField(max_length=2, verbose_name="category_code", unique=True, default="")
    symbol = models.ImageField(blank=True)
    
    class Meta:
        verbose_name_plural = ("Categories")
    
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
    
    @classmethod
    def get_with_category_codes(self, codes):
        args, q = [], models.Q()
        for code in codes: args.append(Category.objects.get(code=code).id)
        for arg in args: q |= models.Q(category = arg)
        return self.objects.filter(q)
    
    @classmethod
    def buy(self, item_id, user):
        item = Item.objects.get(id = item_id)
        item.closed = True
        item.buyer = user
        item.save()
        
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
        
    def serialize(self):
        return loads(serialize('json', [self,]))
