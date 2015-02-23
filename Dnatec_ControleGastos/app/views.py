
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from app.models import *
from app.forms import *
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants as msg
from app.views import redirect
from django.db import models
from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
import StringIO
import zipfile
from django.core.files.uploadedfile import TemporaryUploadedFile, InMemoryUploadedFile
from wsgiref.util import FileWrapper
import os

def home(request):

    if  request.user.is_authenticated():
        contabanco = ContaBanco.objects.all()
        return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Bem vindo ao sistema de controle de gastos!',
            'contas' : contabanco,
        }))  
    else:
        return redirect('django.contrib.auth.views.login')

def about(request):
    
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'Controle de gastos',
            'message':'Aplicacao de controle de gastos do projeto DNATEC desenvolvido por Alex Duzi',
        }))


def novacontarender(request):

    if  request.user.is_authenticated():
        return render(
            request,
            'app/novaconta.html',
            context_instance = RequestContext(request,
            {
                'title': 'Cadastro de nova conta',
                'form': BootstrapNovaContaForm,
            })
        )
    else:
        return redirect('django.contrib.auth.views.login')


def novogastorender(request,contaid):

    if  request.user.is_authenticated():
        contabanco = ContaBanco.objects.get(id=contaid)
        gastos = contabanco.gastos.all()
        return render(
            request,
            'app/novogasto.html',
            context_instance = RequestContext(request,
            {
                'title': 'Cadastro de novo gasto',
                'form': BootstrapNovoGastoForm,
                'conta': contabanco,
                'gastos': gastos,
            })
        )
    else:
        return redirect('django.contrib.auth.views.login')

def downloadarquivo(request,contaid):

    if  request.user.is_authenticated():
        contabanco = ContaBanco.objects.get(id=contaid)
        
        filename = contabanco.arquivo.name                                
        wrapper = FileWrapper(file(filename))
        response = HttpResponse(wrapper, content_type='text/plain')
        response['Content-Length'] = os.path.getsize(filename)
        return response

def novopagamentorender(request,gastoid):
    
    if  request.user.is_authenticated():
        return render(
            request,
            'app/novopagamento.html',
            context_instance = RequestContext(request,
            {
                'title': 'Cadastro de novo pagamento',
                'form': BootstrapNovoPagamentoForm,
            })
        )
    else:
        return redirect('django.contrib.auth.views.login')



def novacontainsert(request):

    form = BootstrapNovaContaForm(request.POST, request.FILES)
    if form.is_valid():
        banco = ContaBanco()
        banco.nome_banco = request.POST['nome_banco']
        banco.conta = request.POST['conta']
        banco.agencia = request.POST['agencia']
        banco.saldo_conta_corrente = request.POST['saldo_conta_corrente']
        banco.arquivo = request.FILES['arquivo']
        banco.save()
        messages.success(request, 'Nova conta adicionada!')
        return redirect('home')
    else:
        messages.error(request, 'Gasto nao pode ser incluido!')
        return redirect('novacontarender')

def novogastoinsert(request, contaid):

    form = BootstrapNovoGastoForm(request.POST)
    if form.is_valid():
        contabanco = get_object_or_404(ContaBanco, pk=contaid)
        pagamento = Pagamento(pago=False, data = datetime.now())
        pagamento.save()
        gasto = Gasto()
        gasto.nome = request.POST['gasto']
        dataPosted = datetime.strptime(request.POST['data'], '%m/%d/%Y')
        gasto.data = dataPosted.strftime('%Y-%m-%d')
        gasto.valor = request.POST['valor']
        gasto.descricao = request.POST['descricao']
        gasto.pagamento = pagamento
        gasto.save()
        contabanco.gastos.add(gasto)
        contabanco.save()
        messages.success(request, 'Novo gasto adicionado!')
        return HttpResponseRedirect(reverse("novogasto", args=[contaid]))
        #return redirect('app.views.novogastorender/'+contaid)
    else:
        messages.error(request, 'Gasto nao pode ser incluido!')
        return redirect('app.views.novacontarender')

def novopagamentoinsert(request, gastoid):

    form = BootstrapNovoPagamentoForm(request.POST)
    if form.is_valid():
        gasto = Gasto.objects.get(id=gastoid)
        pagamento = Pagamento()
        gasto.pago = request.POST['pago']
        gasto.data = request.POST['data']
        gasto.save()
        gasto.pagamento = pagamento
        gasto.save()
        messages.success(request, 'Novo gasto adicionado!')
        return redirect('app.views.home')
    else:
        messages.error(request, 'Pagamento nao pode ser incluido!')
        return redirect('app.views.novacontarender')