from django import template
from Task.models import Task
register = template.Library()

@register.filter(name='nToPeriodicity')
def nToPeriodicity(n):
    periodicity = ''
    
    match n:
        case 0:
            periodicity = 'No periodico'
        case 1:
            periodicity = 'Diario'
        case 2:
            periodicity = 'Semanal'
        case 3:
            periodicity = 'Mensual'
        case 4:
            periodicity = 'Anual'
    return periodicity