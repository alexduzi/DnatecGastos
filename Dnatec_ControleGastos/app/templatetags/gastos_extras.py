from django import template

register = template.Library()



@register.inclusion_tag('contaspartial.html')
def mostra_contas(contabanco):
    return {'contas': contabanco}


@register.inclusion_tag('gastospartial.html')
def mostra_gastos(gastos):
    return {'gastos': gastos}

register.inclusion_tag('app/contaspartial.html')(mostra_contas)
register.inclusion_tag('app/gastospartial.html')(mostra_gastos)