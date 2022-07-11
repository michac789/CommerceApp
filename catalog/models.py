from django.db import models
from sso.models import User


# class ItemOrdered(models.Model):
#     id = models.AutoField(primary_key=True)
    
class CommentTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=256, blank=False, null=False)
    time = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Comment(CommentTemplate):
    pass


class Reply(CommentTemplate):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
