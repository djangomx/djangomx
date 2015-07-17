#coding: utf-8
from django.forms import ModelForm
from django import forms
from .models import Job


class JobForm(ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
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
