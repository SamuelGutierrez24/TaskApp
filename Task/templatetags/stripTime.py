from django import template
from datetime import datetime
register = template.Library()

@register.filter(name='stripTime')
def stripTime(time):
    return time.__str__()