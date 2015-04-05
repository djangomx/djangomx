from django import forms
from django.forms.util import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from .models import NewsletterSubscription


User = get_user_model()


class NewsletterForm(forms.ModelForm):
    """ This is the base class for all forms managing subscriptions. """

    class Meta:
        model = NewsletterSubscription
        fields = ('name', 'email')

    def __init__(self, *args, **kwargs):

        assert 'newsletter' in kwargs, 'No newsletter specified'

        newsletter = kwargs.pop('newsletter')

        if 'ip' in kwargs:
            ip = kwargs['ip']
            del kwargs['ip']
        else:
            ip = None

        super(NewsletterForm, self).__init__(*args, **kwargs)

        self.instance.newsletter = newsletter

        if ip:
            self.instance.ip = ip


class SubscribeRequestForm(NewsletterForm):
    """
    Request subscription to the newsletter. Will result in an activation email
    being sent with a link where one can edit, confirm and activate one's
    subscription.
    """

    def clean_email_field(self):
        data = self.cleaned_data['email_field']

        if not data:
            raise ValidationError(_("An e-mail address is required."))

        # Check whether we should be subscribed to as a user
        try:
            user = User.objects.get(email__exact=data)

            raise ValidationError(_(
                "The e-mail address '%(email)s' belongs to a user with an "
                "account on this site. Please log in as that user "
                "and try again."
            ) % {'email': user.email})

        except User.DoesNotExist:
            pass

        # Check whether we have already been subscribed to
        try:
            subscription = NewsletterSubscription.objects.get(
                email_field__exact=data,
                newsletter=self.instance.newsletter
            )

            if subscription.subscribed and not subscription.unsubscribed:
                raise ValidationError(
                    _("Your e-mail address has already been subscribed to.")
                )
            else:
                self.instance = subscription

            self.instance = subscription

        except NewsletterSubscription.DoesNotExist:
            pass

        return data
