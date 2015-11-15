# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
