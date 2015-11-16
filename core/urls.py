# -*- encoding: utf-8 -*-
from django.conf.urls import include, url
from tastypie.api import Api
from . import views
from api import *

v1_api = Api(api_name='v1')
v1_api.register(ClienteResource())
v1_api.register(TelefoneResource())
v1_api.register(ProjetoResource())
v1_api.register(HorasTrabalhoResource())
v1_api.register(InvoiceResource())

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^cliente/', include([
        url(r'^$', views.cliente_lista),
        url(r'^novo/$', views.cliente_novo),
        url(r'^editar/(?P<slug>[\w-]+)$', views.cliente_editar),
        url(r'^salvar/$', views.cliente_salvar, {'id':None}),
        url(r'^salvar/(?P<id>\w+)/$', views.cliente_salvar),
    ])),

    url(r'^api/', include(v1_api.urls)),

    url(r'^forms$', views.forms),
    url(r'^tables$', views.tables),
]
