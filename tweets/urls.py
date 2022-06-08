from django.urls import path, include
from .views import NewsTweetCreateView

urlpatterns = [
    path("newsTweet/create/", NewsTweetCreateView.as_view(), name = "createNewsTweet"),
    
]