#coding: utf-8
from annoying.decorators import render_to


@render_to("contact_home.html")
def contact_home(request):
    return {}
