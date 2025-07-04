from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Return dictionary[key] or None if key doesn't exist"""
    return dictionary.get(key)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_attr(obj, attr_name):
    return getattr(obj, attr_name, '')