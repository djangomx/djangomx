#coding: utf-8
from django.contrib import admin
from project.models import Type, Skill, Level, Project


class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'is_active',)


class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'is_active',)


class LevelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'is_active',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active',)

admin.site.register(Type, TypeAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Project, ProjectAdmin)
