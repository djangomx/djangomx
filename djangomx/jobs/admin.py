# coding: utf-8
from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'content', 'contact', 'is_active', 'is_approved',)
    list_editable = ('is_approved', 'is_active',)
    search_fields = ('title',)

admin.site.register(Job, JobAdmin)
