
from django import forms
from django.contrib.auth.forms import *
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, request = None, *args, **kwargs):
        return super(BootstrapAuthenticationForm, self).__init__(request, *args, **kwargs)

    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class BootstrapNovaContaForm(forms.Form):
    

    nome_banco = forms.CharField(label=_("Nome banco"),
                                max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Nome banco'}))
    agencia = forms.CharField(label=_("Agencia"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Agencia'}))
    conta = forms.CharField(label=_("Conta"),
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder':'Conta'}))
    saldo_conta_corrente = forms.FloatField(label=_("Saldo"),
                                widget=forms.NumberInput({
                                    'class': 'form-control',
                                    'placeholder':'Saldo'}))


class BootstrapNovoGastoForm(forms.Form):
    
    gasto = forms.CharField(label=_("Nome do gasto"),
                                max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Nome do gasto'}))
    data = forms.DateField(label=_("Data em que foi efetuado o gasto"),
                               widget=forms.DateInput({
                                   'date-input' : 'true',
                                   'class': 'form-control',
                                   'placeholder':'data'}))
    valor = forms.FloatField(label=_("Valor"),
                                widget=forms.NumberInput({
                                    'class': 'form-control',
                                    'placeholder':'Valor'}))
    descricao = forms.CharField(label=_("Descricao"),
                                widget=forms.Textarea({
                                    'class': 'form-control',
                                    'placeholder':'Descricao'}))

class BootstrapNovoPagamentoForm(forms.Form):
    
    pago = forms.BooleanField(label=_("Pago"),
                               widget=forms.CheckboxInput({
                                   'class': 'form-control',
                                   'placeholder': 'Pago'}))
    data = forms.DateField(label=_("Agencia"),
                               widget=forms.DateInput({
                                   'date-input' : 'true',
                                   'class': 'form-control',
                                   'placeholder':'Data'}))