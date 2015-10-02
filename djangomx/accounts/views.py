# coding: utf-8
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from annoying.decorators import render_to


@render_to("accounts/profile.html")
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return {'user': user}


@render_to("home.html")
def home(request):
    """ Renders django.mx home page """
    return {}
