from django.shortcuts import render

# Create your views here.

from .models import NewsTweet, OpinionTweet
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView

class NewsTweetCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = NewsTweet
    fields = ['subject', 'text']
    template_name = "tweets/createNewsTweet.html"
    login_url = "account_login"
    permission_required = "newstweets.create_permission"