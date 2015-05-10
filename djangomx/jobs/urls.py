# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'jobs.views',
    url(r'^$', 'jobs_home', name='jobs_home'),
    url(r'^nueva$', 'new_job', name='new_job'),
)
