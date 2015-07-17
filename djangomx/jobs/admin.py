#coding: utf-8
from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'content', 'contact', 'active', 'aproved',)
    list_editable = ('aproved', 'active',)
    search_fields = ('title',)

admin.site.register(Job, JobAdmin)
