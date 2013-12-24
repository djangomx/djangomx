#coding: utf-8
from django.forms import ModelForm
from django import forms
from redactor.widgets import RedactorEditor

from .models import Job


class JobForm(ModelForm):
    content = forms.CharField(
        widget=RedactorEditor(
            redactor_css="/static/css/redactor.css",
            redactor_settings={
                'autoformat': True,
                'overlay': False,
                'minHeight': 200,
                'buttons': ['bold', 'italic', 'unorderedlist', 'underline']
            }
        )
    )

    class Meta:
        model = Job
        exclude = (
            'slug',
            'created_at',
            'update_at',
            'active',
            'aproved',
        )
