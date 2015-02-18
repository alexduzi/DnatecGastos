
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import *
from app.forms import *
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants as msg
from app.views import redirect


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
        return render(
            request,
            'app/novogasto.html',
            context_instance = RequestContext(request,
            {
                'title': 'Cadastro de novo gasto',
                'form': BootstrapNovoGastoForm,
                'conta': contabanco
            })
        )
    else:
        return redirect('django.contrib.auth.views.login')


def novopagamentorender(request):
    
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

    storage = messages.get_messages(request)
    storage.used = False

    form = BootstrapNovaContaForm(request.POST)
    if form.is_valid():
        banco = ContaBanco()
        banco.nome_banco = request.POST['nome_banco']
        banco.conta = request.POST['conta']
        banco.agencia = request.POST['agencia']
        banco.saldo_conta_corrente = request.POST['saldo_conta_corrente']
        banco.save()
        messages.success(request, 'Nova conta adicionada!')
        return redirect('app.views.home')
    else:
        messages.error(request, 'Gasto nao pode ser incluido!')
        return redirect('app.views.novacontarender')

def novogastoinsert(request, contaid):

    storage = messages.get_messages(request)
    storage.used = False

    form = BootstrapNovaContaForm(request.POST)
    if form.is_valid():
        contabanco = ContaBanco.objects.get(id=contaid)
        gasto = Gasto()
        gasto.nome = request.POST['nome']
        gasto.data = request.POST['data']
        gasto.valor = request.POST['valor']
        gasto.descricao = request.POST['descricao']
        gasto.save()
        contabanco.gastos.add(gasto)
        contabanco.save()
        messages.success(request, 'Novo gasto adicionado!')
        return redirect('app.views.novogastorender/'+contaid)
    else:
        messages.error(request, 'Gasto nao pode ser incluido!')
        return redirect('app.views.novacontarender')

def novopagamentoinsert(request, gastoid):

    storage = messages.get_messages(request)
    storage.used = False

    form = BootstrapNovaContaForm(request.POST)
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