from django import template
from niker.models import Shoes

register = template.Library()

@register.inclusion_tag('niker/tags/last_added_shoes.html')
def get_last_added(count=15):
    shoes = Shoes.objects.order_by('id')[:count]
    return {'last_shoes': shoes}