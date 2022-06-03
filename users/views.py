from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView
# Create your views here.


class ProfileView(UpdateView):

    model = get_user_model()
    template_name = "account/profile.html"
    fields = ["email", "profilePic"]
    
