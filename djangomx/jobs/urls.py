#coding: utf-8
try:
    from django.conf.urls import patterns, url
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    'jobs.views',
    url(r'^$', 'jobs_home', name='jobs_home'),
    url(r'^nueva$', 'new_job', name='new_job'),
)
