# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=50, db_index=True)),
                ('email', models.CharField(unique=True, max_length=60, db_index=True)),
                ('bio', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creaci\xf3n')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Activo')),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Usuario',
            },
        ),
    ]
