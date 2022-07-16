from django.db import models
from sso.models import User
from myshop.models import Item


class ItemOrdered(models.Model):
    id = models.AutoField(primary_key=True)
    
    class Meta: verbose_name_plural = ("Items Ordered")
