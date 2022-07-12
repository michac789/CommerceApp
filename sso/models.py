from django.db import models
from django.contrib.auth.models import AbstractUser
from markdown2 import markdown


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


class NonStrippingTextField(models.TextField):
    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingTextField, self).formfield(**kwargs)
    

class AdminPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    markdown = NonStrippingTextField()
    time_created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = ("Admin Posts")
    
    def __str__(self):
        return f"<Admin Post ID {self.id}: {self.title}>"
    
    def serialize(self):
        return {
            "id": self.id,
            "creator": self.creator.username,
            "title": self.title,
            "markdown": markdown(self.markdown),
            "time": self.time_created.strftime("%b %d %Y, %I:%M %p"),
        }
