
from .models import NewsTweet, OpinionTweet

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView

class NewsTweetCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = NewsTweet
    fields = ['subject', 'text']
    template_name = "tweets/createNewsTweet.html"
    login_url = "account_login"
    permission_required = "newstweets.create_permission"
    success_url = "/"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        print(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.author = self.request.user
        self.object.save()
        return super(NewsTweetCreateView, self).form_valid(form)


