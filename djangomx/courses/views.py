#coding: utf-8
from annoying.decorators import render_to


@render_to("courses_home.html")
def courses_home(request):
    return {}
