#coding: utf-8

try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *


from .views import LatestEntriesFeed

urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'blog_home', name='blog_home'),



    url(r'^categoria/(?P<category_slug>[-\w]+)/$',
        'category',
        name='category'),

    url(r'^archivos/$', 'archives', name='archives'),

    (r'^feed/$', LatestEntriesFeed()),

    url(r'^entrada/(?P<slug>[-\w]+)/$', 'view_post',
        name='view_post'),
)
