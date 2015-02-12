

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):

    if  request.user.is_authenticated():
        return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Bem vindo ao sistema de controle de gastos!',
        }))   

    return render(request,
                'app/login.html',
                context_instance = RequestContext(request,
                {
                    'title':'',
                }))
    

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