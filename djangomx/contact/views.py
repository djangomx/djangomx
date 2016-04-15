# coding: utf-8
from django.core.mail import send_mail
from annoying.decorators import render_to
from django.conf import settings
from .forms import ContactForm


@render_to("contact_home.html")
def contact_home(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Nueva oferta de trabajo',
                'https://django.mx/admin/jobs/',
                settings.DEFAULT_FROM_EMAIL,
                [settings.NOTIFICATION_EMAIL],
                fail_silently=False
            )
    else:
        form = ContactForm()
    return {'form': form}
