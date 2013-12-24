#coding: utf-8
from django.contrib import admin
from django.db import models
from redactor import widgets
from models import Job


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'content', 'contact', 'active', 'aproved',)
    list_editable = ('aproved', 'active',)
    search_fields = ('title',)

    formfield_overrides = {
        models.TextField: {'widget': widgets.AdminRedactorEditor()},
    }

admin.site.register(Job, JobAdmin)
