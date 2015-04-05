# coding: utf-8
from django.contrib import admin
from .models import NewsletterSubscription


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'create_date')

admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)
