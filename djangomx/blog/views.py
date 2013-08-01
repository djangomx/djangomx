#coding: utf-8
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from annoying.decorators import render_to
from django.shortcuts import get_object_or_404
from blog.models import Category, Post


@render_to('index.html')
def home(request):
    """
    The index for blog. Get the necessary information to show the
    Category and date archives in the sidebar, and then load a full page
    of Posts using django' built in pagination.
    """

    # Get the blog posts and order desc
    archive_dates = Post.objects.dates('date_publish', 'month', order='DESC')

    # Get all categories
    categories =  Category.objects.all()

    page = request.GET.get('page')
    post_queryset = Post.objects.all().order_by('-date_publish')
    paginator = Paginator(post_queryset, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of resutls
        posts = paginator.page(paginator.num_pages)

    return {
        'posts': posts,
        'archive_dates': archive_dates,
        'categories': categories,
    }


@render_to('single.html')
def single(request, slug):
    """
    The sinle article. The single view loads all of the necessary blog archive sidebar variables.
    Additionally, it selects the Post indicated by the slug in the url rule.
    """

    # Get the post item that comes in the slug url
    post = get_object_or_404(Post, slug=slug)

    # Get the blog posts and order desc
    archive_dates = Post.objects.dates('date_publish', 'month', order='DESC')

    # Get all categories
    categories = Category.objects.all()

    return {
        'post': post,
        'archive_dates': archive_dates,
        'categories': categories,
    }


@render_to('category-archive.html')
def category_archive(request, slug):
    """
    The archive by category view
    """
    archive_dates = Post.objects.dates('date_publish', 'month', order='DESC')
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)

    # Pagination
    page = request.GET.get('page')
    blog_queryset = Post.objects.filter(categories=category)
    paginator = Paginator(blog_queryset, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of resutls
        posts = paginator.page(paginator.num_pages)

    return {
        'posts': posts,
        'archive_dates': archive_dates,
        'categories': categories,
        'category': category,
    }