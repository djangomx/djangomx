#coding: utf-8
from annoying.decorators import render_to


@render_to("jobs_home.html")
def jobs_home(request):
    return {}
