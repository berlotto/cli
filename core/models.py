# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.text import slugify


TIPO_TELEFONE = (
    ('celular',"Móvel Pessoal"),
    ('celular-profissional',"Móvel Profissional"),
    ('fixo',"Fixo"),
    ('fixo-residencial',"Fixo Residencial"),
    ('fixo-comercial',"Fixo Comercial"),
)

OPERADORAS = (
        ('claro',"Claro"),
        ('vivo',"Vivo"),
        ('tim',"Tim"),
        ('oi',"Oi"),
        ('nextel',"Nextel"),
        ('ctbc',"CTBC Telecom"),
        ('porto',"Porto Seguro Conecta"),
        ('sercomtel',"Sercomtel"),
)

DDD_BRASIL = tuple( [(str(x),str(x)) for x in range(11,100)] )

FORMA_PAGTO = (
        ("deposito","Depósito em CC"),
        ("paypal","Paypal"),
        ("pagseguro","Pagseguro"),
        ("maos","Em mãos"),
        ("bitcoins","Bitcoins"),
        ("free","Não cobrado"),
        ("troca","Troca"),
)

class BaseModel(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)


class Telefone(BaseModel):
    """Dados telefonicos do cliente"""
    numero = models.CharField(max_length=50)
    ddd = models.CharField(max_length=5, choices=DDD_BRASIL)
    tipo = models.CharField(max_length=35, choices=TIPO_TELEFONE)
    operadora = models.CharField(max_length=50, choices=OPERADORAS)
    whatsapp = models.BooleanField(default=False)

class Cliente(BaseModel):
    """Os clientes"""
    nome = models.CharField(max_length=255)
    nome_contato = models.CharField(max_length=255)
    telefone = models.ForeignKey(Telefone)
    email = models.EmailField()
    skype = models.CharField(max_length=1255, blank=True)
    facebook = models.CharField(max_length=1255, blank=True)
    twitter = models.CharField(max_length=1255, blank=True)
    linkedin = models.CharField(max_length=1255, blank=True)
    google_plus = models.CharField(max_length=1255, blank=True)
    slug = models.SlugField(unique=True)


class Projeto(BaseModel):
    """Projeto"""
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=2000, null=True, blank=True)
    valor_hora = models.PositiveSmallIntegerField()
    cliente = models.ForeignKey(Cliente)
    slug = models.SlugField(unique=True)


class HorasTrabalho(BaseModel):
    """Hora de trabalho feita"""
    projeto = models.ForeignKey(Projeto)
    quantidade = models.PositiveSmallIntegerField()
    valor_promocional = models.PositiveSmallIntegerField()
    resumo = models.CharField(max_length=800)


class DadosPagto(BaseModel):
    """Dados informativos da conta ou forma de pagto"""
    descricao = models.TextField(max_length=4000)
    forma_pagto = models.CharField(max_length=100, choices=FORMA_PAGTO)


class Invoice(BaseModel):
    """Invoices gerados e enviados aos clientes"""
    cliente = models.ForeignKey(Cliente)
    numero = models.PositiveIntegerField()
    horas = models.ManyToManyField(HorasTrabalho)
    email_alternativo = models.EmailField()
    enviado = models.BooleanField()
    forma_pagto = models.CharField(max_length=100, choices=FORMA_PAGTO)
    slug = models.SlugField(unique=True)

    def get_full_name(self):
        return self.cliente.nome + "{:04d}".format(self.numero)

