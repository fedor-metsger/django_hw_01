# dogs/templatetags/my_tags.py

import datetime
from django import template

register = template.Library()

# Создание тега
@register.simple_tag
def media_tag(fname):
    return "/media/" + str(fname)


# Создание фильтра
@register.filter
def media_filter(fname):
    return "/media/" + str(fname)