# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'accounts.views',
    url(r'^(?P<username>\w+)$', 'profile', name='profile'),
)
