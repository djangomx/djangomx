# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^@(?P<username>\w+)$', views.profile, name='profile'),

]
