#coding: utf-8
from annoying.decorators import render_to


@render_to("blog_home.html")
def blog_home(request):
    return {}
