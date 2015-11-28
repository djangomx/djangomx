# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20151127_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='aproved',
            new_name='is_approved',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='job',
            name='content',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(unique=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=75),
        ),
    ]
