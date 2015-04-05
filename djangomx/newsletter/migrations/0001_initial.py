# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterNewsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(unique=True, max_length=50)),
                ('email', models.CharField(max_length=75)),
                ('sender', models.CharField(max_length=200)),
                ('visible', models.IntegerField()),
                ('send_html', models.IntegerField()),
            ],
            options={
                'db_table': 'newsletter_newsletter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('ip', models.CharField(max_length=15, null=True, blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('activation_code', models.CharField(max_length=40)),
                ('subscribed', models.IntegerField()),
                ('subscribe_date', models.DateTimeField(null=True, blank=True)),
                ('unsubscribed', models.IntegerField(default=False)),
                ('unsubscribe_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'newsletter_subscription',
                'managed': False,
            },
        ),
    ]
