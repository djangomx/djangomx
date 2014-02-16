#coding: utf-8

try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'blog_home', name='blog_home'),
)
