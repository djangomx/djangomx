# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'avatars', blank=True)),
                ('cover', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'covers', blank=True)),
                ('bio', models.TextField(null=True, blank=True)),
                ('github', models.URLField(null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('facebook', models.URLField(null=True, blank=True)),
                ('linkedin', models.URLField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
