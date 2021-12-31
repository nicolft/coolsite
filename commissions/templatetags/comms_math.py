from django import template
register = template.Library()

@register.filter
def idiv(value, arg):
    """value // arg"""
    return value // arg
    # TODO write exception handling

@register.filter
def bitmask(value, arg):
    """value & arg"""
    return value & arg
    # TODO write exception handling