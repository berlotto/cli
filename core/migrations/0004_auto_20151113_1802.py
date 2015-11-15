# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151113_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefone',
            name='whatsapp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='tipo',
            field=models.CharField(max_length=35, choices=[(b'celular', b'M\xc3\xb3vel Pessoal'), (b'celular-profissional', b'M\xc3\xb3vel Profissional'), (b'fixo', b'Fixo'), (b'fixo-residencial', b'Fixo Residencial'), (b'fixo-comercial', b'Fixo Comercial')]),
        ),
    ]
