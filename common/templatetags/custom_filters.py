# templatetags/custom_filters.py
from django import template
import re

register = template.Library()

@register.filter
def split_attrs(attrs_string):
    pattern = r'(\w+)(?:="([^"]*)")?\s*'
    return re.findall(pattern, attrs_string)