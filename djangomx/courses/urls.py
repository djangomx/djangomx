#coding: utf-8
try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

urlpatterns = patterns(
    'courses.views',
    url(r'^$', 'courses_home', name='courses_home'),
)
