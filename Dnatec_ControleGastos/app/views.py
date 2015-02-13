
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

@login_required(login_url='/login/')
def home(request):

    if  request.user.is_authenticated():
        return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Bem vindo ao sistema de controle de gastos!',
        }))   

    return cre(request)
    

def about(request):
    
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'Controle de gastos',
            'message':'Aplicacao de controle de gastos do projeto DNATEC desenvolvido por Alex Duzi',
        })
    )

@login_required(login_url='/login/')
def contas(request):
    
    return render(
        request,
        'app/contas.html',
        context_instance = RequestContext(request,
        {
            'title':'Contas cadastradas',
            'message':'',
        })
    )

@login_required(login_url='/login/')
def novaconta(request):
    
    return render(
        request,
        'app/novaconta.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de nova conta',
            'message':'',
        })
    )