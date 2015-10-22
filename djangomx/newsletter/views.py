# coding: utf-8
import mailchimp

from django.conf import settings

from annoying.decorators import ajax_request

from .forms import NewsletterForm
from .models import Subscription


@ajax_request
def subscribe_request(request):
    """ Adds a new subscription to mailchimp list. """
    if request.POST:
        mail_chimp = mailchimp.Mailchimp(
            settings.SECRETS['mailchimp_api_key']
        )
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscription = Subscription(email=email)
            subscription.save()
            try:
                mail_chimp.lists.subscribe(
                    settings.SECRETS['mailchimp_list_id'],
                    {'email': email},
                    double_optin=False,
                    send_welcome=True
                )
            except mailchimp.ListAlreadySubscribedError:
                return {
                    'success': False, 'error': 'Email is already subscribed'
                }
            return {'success': True}
        else:
            return {
                'success': False,
                'error': form.errors.get('email')
            }
    return {'success': False, 'error': 'Request not valid'}
