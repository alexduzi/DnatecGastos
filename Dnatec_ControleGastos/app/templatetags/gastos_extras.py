from django import template

register = template.Library()
register.inclusion_tag('contaspartial.html')


@register.inclusion_tag('contaspartial.html')
def mostra_contas(contabanco):
    return {'contas': contabanco}