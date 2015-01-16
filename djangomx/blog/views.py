# coding: utf-8
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from annoying.decorators import render_to

from blog.models import Category, Post


@render_to("blog_home.html")
def blog_home(request):
    posts_list = Post.objects.filter(is_active=True).order_by('-published_at')
    categories = Category.objects.filter(is_active=True)
    paginator = Paginator(posts_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # IF page is not an intenger, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return {
        'posts': posts,
        'categories': categories,
        'paginator': paginator,
    }


@render_to('post.html')
def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.filter(is_active=True)

    return {
        'post': post,
        'categories': categories,
    }


@render_to('category.html')
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts_list = Post.objects.filter(is_active=True,
        category=category).order_by('-published_at')
    categories = Category.objects.filter(is_active=True)
    paginator = Paginator(posts_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # IF page is not an intenger, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return {
        'category': category,
        'posts': posts,
        'categories': categories,
        'paginator': paginator,
    }


@render_to('archives.html')
def archives(request):
    posts_list = Post.objects.filter(is_active=True).order_by('-published_at')

    years = {
        '2015': [],
    }

    for year in years:
        list_posts = []
        for post in posts_list:
            post_date = post.pub_date.date()
            year_post = post_date.year

            if year_post == int(year):
                list_posts.append(post)

        years[year] = list_posts

    return {
        'archives': years
    }


class LatestEntriesFeed(Feed):
    title = 'Django México'
    link = 'http://django.mx'
    description = 'La comunidad de Django en México'

    def items(self):
        return Post.objects.filter(is_active=True).order_by('-published_at')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('view_post', args=[item.slug])
