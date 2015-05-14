# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 14, 19, 47, 17, 618292, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 14, 19, 47, 21, 802269, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
