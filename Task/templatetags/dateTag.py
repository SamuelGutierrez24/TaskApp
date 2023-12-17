from django import template
register = template.Library()

@register.filter(name='dateTag')
def dateTag(n):
    label = ''
    
    if n==0:
        label = 'Fecha de vencimiento'
    else:
        label = 'Fecha Inicial'
    return label