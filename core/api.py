# -*- encoding: utf-8 -*-
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from models import *


class TelefoneResource(ModelResource):
    class Meta:
        queryset = Telefone.objects.all()
        resource_name = 'telefone'
        authorization = Authorization()

class ClienteResource(ModelResource):
    telefone = fields.ForeignKey(TelefoneResource, 'telefone', null=True, blank=True)
    class Meta:
        queryset = Cliente.objects.all()
        resource_name = 'cliente'
        authorization = Authorization()

class ProjetoResource(ModelResource):
    cliente = fields.ForeignKey(ClienteResource, 'cliente')
    class Meta:
        queryset = Projeto.objects.all()
        resource_name = 'projeto'
        authorization = Authorization()

class HorasTrabalhoResource(ModelResource):
    projeto = fields.ForeignKey(ProjetoResource, "projeto")
    class Meta:
        queryset = HorasTrabalho.objects.all()
        resource_name = 'hora'
        authorization = Authorization()

class InvoiceResource(ModelResource):
    cliente = fields.ForeignKey(ClienteResource, 'cliente')
    horas = fields.ToManyField(HorasTrabalhoResource, 'horas', full=True)
    class Meta:
        queryset = Invoice.objects.all()
        resource_name = 'invoice'
        authorization = Authorization()
