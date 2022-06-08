from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class OpinionTweet(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.CharField(max_length = 280)
    created_at = models.DateTimeField(auto_now_add = True)

class NewsTweet(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    subject = models.CharField(max_length = 100)
    text = models.CharField(max_length = 280)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        permissions = [
            ('create_permission', 'Can write news tweets'),
        ]
