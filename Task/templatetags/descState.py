from django import template
from Task.models import Task
register = template.Library()

@register.filter(name='descState')
def descState(n):
    state = ''
    
    match n:
        case 0:
            state = 'Por hacer'
        case 1:
            state = 'En proceso'
        case 2:
            state = 'Cancelada'
        case 3:
            state = 'Finalizada'
            
    return state