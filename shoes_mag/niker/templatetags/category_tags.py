from django import template
from niker.models import ShoesCategory

register = template.Library()

@register.simple_tag()
def get_categories():
    """Получение всех категорий"""
    return ShoesCategory.objects.all()