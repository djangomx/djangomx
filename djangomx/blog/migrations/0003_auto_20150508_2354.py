# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150508_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='Este es el contenido de el Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='extract',
            field=models.TextField(help_text='Este es solo un resumen de el Post que se muestra en la         lista de posts', blank=True),
        ),
    ]
