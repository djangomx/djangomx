# coding: utf-8
from django.views.generic import DetailView, TemplateView

from blog.models import Post
from .models import Profile


class ProfileView(DetailView):
    """ User profile page """
    template_name = 'accounts/profile.html'
    model = Profile
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        user = self.object.user
        context.update({
            'user': user,
            'posts': Post.objects.filter(author=user)
        })
        return context


class HomeView(TemplateView):
    """ Renders django.mx home page """
    template_name = 'home.html'
