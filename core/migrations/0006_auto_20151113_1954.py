# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151113_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
