#coding: utf-8
from django.contrib import admin
from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'is_active',)
    search_fields = ('title', )


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'author', 'date_publish', 'is_active')
    search_fields = ('title', )
    list_filter = ('categories', )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)