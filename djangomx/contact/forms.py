from django import forms
from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    name = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    subject = forms.CharField(
        label='Asunto',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Contact
        exclude = ('created_at', 'updated_at', 'active')
