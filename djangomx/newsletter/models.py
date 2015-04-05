from django.db import models
from django.conf import settings


class NewsletterNewsletter(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    email = models.CharField(max_length=75)
    sender = models.CharField(max_length=200)
    visible = models.IntegerField()
    send_html = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'newsletter_newsletter'


class NewsletterSubscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    newsletter = models.ForeignKey(NewsletterNewsletter)
    create_date = models.DateTimeField()
    activation_code = models.CharField(max_length=40)
    subscribed = models.IntegerField()
    subscribe_date = models.DateTimeField(blank=True, null=True)
    unsubscribed = models.IntegerField()
    unsubscribe_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_subscription'
