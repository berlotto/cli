# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from forms import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def forms(request):
    return render(request, "forms.html")

def tables(request):
    return render(request, "tables.html")

#============== CLIENTE ====================
def cliente_lista(request):
    clis = Cliente.objects.all()
    variables = RequestContext(request, {
        'clientes': clis
    })
    return render_to_response('cliente/list.html', variables)

def cliente_salvar(request, id=None):
    import pdb; pdb.set_trace()
    if id:
        cli = get_object_or_404(Cliente, id=id)
        clienteform = ClienteForm(request.POST, instance=cli)
        telefoneform = TelefoneForm(request.POST, instance=cli.telefone)
    else:
        clienteform = ClienteForm(request.POST)
        telefoneform = TelefoneForm(request.POST)

    newcli = clienteform.save()
    newtelefone = telefoneform.save()
    newcli.telefone = newtelefone
    newcli.save()

    return redirect('cliente_editar', slug=newcli.slug)

def cliente_editar(request, slug):
    cli = get_object_or_404(Cliente, slug=slug)
    if cli:
        clienteform = ClienteForm(instance=cli)
        telefoneform = TelefoneForm(instance=cli.telefone)
        variables = RequestContext(request, {
            'form': clienteform,
            'telefoneform': telefoneform,
            'cliente': cli,
        })
        return render_to_response('cliente/novo.html', variables)
    else:
        raise Http404("Cliente não existe")

def cliente_novo(request):
    clienteform = ClienteForm()
    telefoneform = TelefoneForm()
    variables = RequestContext(request, {
        'form': clienteform,
        'telefoneform': telefoneform,
    })
    return render_to_response('cliente/novo.html', variables)
    # return render(request, "tables.html")
