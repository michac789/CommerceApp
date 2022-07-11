from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    TIER = [
        ("T4", "Banned User"),
        ("T3", "Standard User"),
        ("T2", "Member User"),
        ("T1", "Administrator")
    ]
    tier = models.CharField(max_length=2, choices=TIER, default="T3")
    
    def __str__(self):
        return self.username
