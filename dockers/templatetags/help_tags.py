from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name = 'replace_line')
@stringfilter
def replace_line_separator(text: str, to: str = '<br>'):
    return text.replace("\n", to)
