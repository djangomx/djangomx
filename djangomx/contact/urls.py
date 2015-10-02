# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.contact_home, name='contact_home'),

]
