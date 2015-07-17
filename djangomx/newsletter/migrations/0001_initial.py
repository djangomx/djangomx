# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('ip', models.CharField(max_length=15, null=True, blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('activation_code', models.CharField(max_length=40, null=True, blank=True)),
                ('subscribed', models.BooleanField(default=True)),
                ('subscribe_date', models.DateTimeField(null=True, blank=True)),
                ('unsubscribed', models.BooleanField(default=False)),
                ('unsubscribe_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
