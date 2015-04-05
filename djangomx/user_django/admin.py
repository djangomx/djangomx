# coding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model
    # These override the definitions to the base UserAdmin
    # that reference specific fields on auth.User
    list_display = ('username', 'email', 'image', 'created_at', 'is_active')
    list_filter = ('username', 'email',)
    fieldsets = (
        ('Usuario', {'fields': ('username', 'email', 'password', 'bio')}),
        ('Permissions', {'fields': ('is_admin', 'groups')}),
        ('Logs', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',
                       'email',
                       'password1',
                       'password2',
                       'bio')}
                ),
        )
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
