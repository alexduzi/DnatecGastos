"""
Definition of urls for Dnatec_ControleGastos.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import *

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^about', 'app.views.about', name='about'),
    #url(r'^contas', 'app.views.contas', name='contas'),
    url(r'^novacontainsert', 'app.views.novacontainsert', name='novacontainsert'),
    url(r'^novaconta$',
        'app.views.novacontarender',
        {
            'template_name': 'app/novaconta.html',
            'nova_conta_form': BootstrapNovaContaForm,
            'extra_context':
            {
                'title':'Cadastro de nova conta',
            }
        },
        name='novacontarender'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
      url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
