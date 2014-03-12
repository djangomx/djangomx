#coding: utf-8
from annoying.decorators import render_to
from models import Post


@render_to("blog_home.html")
def blog_home(request):
    posts = Post.objects.filter(is_active=True)
    return {'posts': posts}
