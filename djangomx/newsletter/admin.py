# coding: utf-8
from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'create_date')

admin.site.register(Subscription, SubscriptionAdmin)
