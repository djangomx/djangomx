# coding: utf-8
from django import forms


class NewsletterForm(forms.Form):
    email = forms.EmailField()
