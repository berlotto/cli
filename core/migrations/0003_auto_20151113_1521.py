# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151112_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.ForeignKey(to='core.Telefone'),
        ),
        migrations.AlterField(
            model_name='dadospagto',
            name='forma_pagto',
            field=models.CharField(max_length=100, choices=[(b'deposito', b'Dep\xc3\xb3sito em CC'), (b'paypal', b'Paypal'), (b'pagseguro', b'Pagseguro'), (b'maos', b'Em m\xc3\xa3os'), (b'bitcoins', b'Bitcoins'), (b'free', b'N\xc3\xa3o cobrado'), (b'troca', b'Troca')]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='forma_pagto',
            field=models.CharField(max_length=100, choices=[(b'deposito', b'Dep\xc3\xb3sito em CC'), (b'paypal', b'Paypal'), (b'pagseguro', b'Pagseguro'), (b'maos', b'Em m\xc3\xa3os'), (b'bitcoins', b'Bitcoins'), (b'free', b'N\xc3\xa3o cobrado'), (b'troca', b'Troca')]),
        ),
    ]
