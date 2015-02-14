from django import template

register = template.Library()



@register.inclusion_tag('contaspartial.html')
def mostra_contas(contabanco):
    return {'contas': contabanco}


register.inclusion_tag('app/contaspartial.html')(mostra_contas)