from django import template
register = template.Library()

@register.filter(name='formatTitle')
def formatTitle(title):
    if(len(title)>18):
        title = (title[:15]+'...')
        
    return title