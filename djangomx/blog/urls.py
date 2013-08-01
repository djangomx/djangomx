#coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),
    url(r'(?P<slug>[-\w]+)/$', 'blog.views.single', name='blog-post-single'),
    url(r'archivo/(?P<slug>[-\w]+)/$', 'blog.views.category_archive', name='blog-category-archive'),
)