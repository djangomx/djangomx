# coding: utf-8
from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', views.jobs_home, name='jobs_home'),
    url(r'^nueva$', views.new_job, name='new_job'),

]
