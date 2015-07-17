# coding: utf-8
from django import forms
from newsletter.models import Subscription


class NewsletterForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if Subscription.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya esta registrado')
        return email
