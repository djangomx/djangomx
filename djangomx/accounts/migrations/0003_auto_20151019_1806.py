# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


def create_gravatars(apps, schema_editor):
    Profile = apps.get_model('accounts', 'Profile')

    for p in Profile.objects.all():
        p.avatar = p.user.email
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150514_1447'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='profile',
            name='_avatar',
            field=models.ImageField(null=True, upload_to=b'avatars', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(create_gravatars),
    ]
