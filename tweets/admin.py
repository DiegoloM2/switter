from django.contrib import admin
from .models import NewsTweet, OpinionTweet, OpinionComment, NewsComment
# Register your models here.

admin.site.register(NewsTweet)
admin.site.register(OpinionTweet)
admin.site.register(OpinionComment)
admin.site.register(NewsComment)
