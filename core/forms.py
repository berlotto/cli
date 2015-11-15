# -*- encoding: utf-8 -*-

from models import *
from django.forms import ModelForm, modelformset_factory, inlineformset_factory

class TelefoneForm(ModelForm):
    class Meta:
        model = Telefone
        fields = ['ddd', 'numero', 'tipo', 'operadora']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'nome_contato', 'telefone', 'email', 'skype', 'facebook', 'twitter', 'linkedin', 'google_plus']

    def save(self):
        instance = super(ClienteForm, self).save(commit=False)
        instance.slug = slugify(instance.nome)
        instance.save()

        return instance

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome','descricao','valor_hora', 'cliente', 'slug']

    def save(self):
        instance = super(ProjetoForm, self).save(commit=False)
        instance.slug = slugify(instance.nome)
        instance.save()

        return instance


class HorasTrabalhoForm(ModelForm):
    class Meta:
        model = HorasTrabalho
        fields = ['projeto', 'quantidade', 'valor_promocional', 'resumo']

class DadosPagtoForm(ModelForm):
    class Meta:
        model = DadosPagto
        fields = ['descricao','forma_pagto']

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['cliente', 'numero','horas','email_alternativo','enviado','forma_pagto','slug']

    def save(self):
        instance = super(InvoiceForm, self).save(commit=False)
        instance.slug = slugify(instance.get_full_name)
        instance.save()

        return instance
