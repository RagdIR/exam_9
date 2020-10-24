from django import template

register = template.Library()


@register.filter
def favorites_by(obj, user):
    return obj.favorites_by(user)