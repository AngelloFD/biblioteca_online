from biblioteca_online.core.models import Libro
from corebc.librobc import get_book_ispn
from django import template

register = template.Library()

@register.filter
def get_book_ispn(ispn)->Libro:
    return get_book_ispn(ispn)
