from django import template

register = template.Library()

@register.filter
def getattribute(obj, attr):
    return getattr(obj, attr, None)

@register.filter
def replace(value, arg):
    """Replaces all occurrences of the first part with the second part.
       Usage: {{ value|replace:"old,new" }}
    """
    old, new = arg.split(',')
    return value.replace(old, new)
