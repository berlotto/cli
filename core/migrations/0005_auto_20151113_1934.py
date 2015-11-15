# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151113_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='facebook',
            field=models.CharField(max_length=1255, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='google_plus',
            field=models.CharField(max_length=1255, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='linkedin',
            field=models.CharField(max_length=1255, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='skype',
            field=models.CharField(max_length=1255, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'nome', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='twitter',
            field=models.CharField(max_length=1255, blank=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'get_full_name', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'nome', unique=True, editable=False),
        ),
    ]
