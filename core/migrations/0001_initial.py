# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('ultima_alteracao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('nome', models.CharField(max_length=255)),
                ('nome_contato', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('skype', models.CharField(max_length=1255)),
                ('facebook', models.CharField(max_length=1255)),
                ('twitter', models.CharField(max_length=1255)),
                ('linkedin', models.CharField(max_length=1255)),
                ('google_plus', models.CharField(max_length=1255)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='DadosPagto',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('descricao', models.TextField(max_length=4000)),
                ('forma_pagto', models.CharField(max_length=100, choices=[(b'deposito', b'Dep\xc3\xb3sito em CC'), (b'paypal', b'Paypal'), (b'pagseguro', b'Pagseguro'), (b'bitcoins', b'Bitcoins'), (b'maos', b'Em m\xc3\xa3os'), (b'free', b'N\xc3\xa3o cobrado'), (b'troca', b'Troca')])),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='HorasTrabalho',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('quantidade', models.PositiveSmallIntegerField()),
                ('valor_promocional', models.PositiveSmallIntegerField()),
                ('resumo', models.CharField(max_length=800)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('numero', models.PositiveIntegerField()),
                ('email_alternativo', models.EmailField(max_length=254)),
                ('enviado', models.BooleanField()),
                ('forma_pagto', models.CharField(max_length=100, choices=[(b'deposito', b'Dep\xc3\xb3sito em CC'), (b'paypal', b'Paypal'), (b'pagseguro', b'Pagseguro'), (b'bitcoins', b'Bitcoins'), (b'maos', b'Em m\xc3\xa3os'), (b'free', b'N\xc3\xa3o cobrado'), (b'troca', b'Troca')])),
                ('cliente', models.ForeignKey(to='core.Cliente')),
                ('horas', models.ManyToManyField(to='core.HorasTrabalho')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(max_length=2000, null=True, blank=True)),
                ('valor_hora', models.PositiveSmallIntegerField()),
                ('cliente', models.ForeignKey(to='core.Cliente')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('numero', models.CharField(max_length=50)),
                ('ddd', models.CharField(max_length=5, choices=[(b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31'), (b'32', b'32'), (b'33', b'33'), (b'34', b'34'), (b'35', b'35'), (b'36', b'36'), (b'37', b'37'), (b'38', b'38'), (b'39', b'39'), (b'40', b'40'), (b'41', b'41'), (b'42', b'42'), (b'43', b'43'), (b'44', b'44'), (b'45', b'45'), (b'46', b'46'), (b'47', b'47'), (b'48', b'48'), (b'49', b'49'), (b'50', b'50'), (b'51', b'51'), (b'52', b'52'), (b'53', b'53'), (b'54', b'54'), (b'55', b'55'), (b'56', b'56'), (b'57', b'57'), (b'58', b'58'), (b'59', b'59'), (b'60', b'60'), (b'61', b'61'), (b'62', b'62'), (b'63', b'63'), (b'64', b'64'), (b'65', b'65'), (b'66', b'66'), (b'67', b'67'), (b'68', b'68'), (b'69', b'69'), (b'70', b'70'), (b'71', b'71'), (b'72', b'72'), (b'73', b'73'), (b'74', b'74'), (b'75', b'75'), (b'76', b'76'), (b'77', b'77'), (b'78', b'78'), (b'79', b'79'), (b'80', b'80'), (b'81', b'81'), (b'82', b'82'), (b'83', b'83'), (b'84', b'84'), (b'85', b'85'), (b'86', b'86'), (b'87', b'87'), (b'88', b'88'), (b'89', b'89'), (b'90', b'90'), (b'91', b'91'), (b'92', b'92'), (b'93', b'93'), (b'94', b'94'), (b'95', b'95'), (b'96', b'96'), (b'97', b'97'), (b'98', b'98'), (b'99', b'99')])),
                ('tipo', models.CharField(max_length=35, choices=[(b'celular', b'Celular'), (b'fixo', b'Fixo'), (b'nextel', b'Nextel')])),
                ('operadora', models.CharField(max_length=50, choices=[(b'claro', b'Claro'), (b'vivo', b'Vivo'), (b'tim', b'Tim'), (b'oi', b'Oi'), (b'nextel', b'Nextel'), (b'ctbc', b'CTBC Telecom'), (b'porto', b'Porto Seguro Conecta'), (b'sercomtel', b'Sercomtel')])),
            ],
            bases=('core.basemodel',),
        ),
        migrations.AddField(
            model_name='horastrabalho',
            name='projeto',
            field=models.ForeignKey(to='core.Projeto'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.OneToOneField(to='core.Telefone'),
        ),
    ]
