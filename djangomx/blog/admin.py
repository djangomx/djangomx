#coding: utf-8
from django.contrib import admin
from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'created_at', 'is_active')


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'created_at', 'is_active')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
