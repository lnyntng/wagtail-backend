from datetime import date
from django import template
from django.conf import settings

from home.models import HomePage

register = template.Library()


@register.inclusion_tag('home/tags/top_menu.html', takes_context=True)
def top_menu(context):
    pages = HomePage.objects.live()

    return {
        'pages': pages,
        'request': context['request'],
    }
