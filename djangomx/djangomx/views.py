# coding: utf-8
from annoying.decorators import render_to, ajax_request
from newsletter.forms import SubscribeRequestForm
from newsletter.models import NewsletterNewsletter


@ajax_request
def subscribe_request(request):
    """ Adds a new subscription """
    newsletter = NewsletterNewsletter.objects.get(id=1)
    if request.POST:
        form = SubscribeRequestForm(
            newsletter=newsletter, data=request.POST
        )
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.subscribed = True
            subscription.save()
            return {'success': True}
        else:
            return {'success': False}
    return {'success': False, 'error': 'Request not valid'}


@render_to("home.html")
def home(request):
    """ Renders django.mx home page """
    return {}
