# -*- encoding: utf-8 -*-
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^cliente/', include([
        url(r'^$', views.lista),
        url(r'^novo/$', views.cliente_novo),
        url(r'^editar/(?P<slug>[\w-]+)$', views.cliente_editar),
        url(r'^salvar/$', views.cliente_salvar, {'id':None}),
        url(r'^salvar/(?P<id>\w+)/$', views.cliente_salvar),
    ])),

    url(r'^forms$', views.forms),
    url(r'^tables$', views.tables),
]
