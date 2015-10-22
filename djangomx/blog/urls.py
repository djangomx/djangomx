# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.blog_home, name='blog_home'),
    url(r'^categoria/(?P<category_slug>[-\w]+)/$', views.category, name='category'),
    url(r'^archivos/$', views.archives, name='archives'),
    url(r'^feed/$', views.LatestEntriesFeed()),
    url(r'^entrada/(?P<slug>[-\w]+)/$', views.view_post, name='view_post'),

]
