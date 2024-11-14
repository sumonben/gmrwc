from django import template
from teacher.models import Teacher

register = template.Library()

@register.filter()
def counter_next(teachers,current_index):
    try:
        return int(current_index)+3 # access the next element
    except:
        return '' # return empty string in case of exception



@register.filter()
def next(teachers, current_index):
    """
    Returns the next element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return teachers[int(current_index) + 1] # access the next element
    except:
        return '' # return empty string in case of exception

@register.filter()
def previous(teachers, current_index):
    """
    Returns the previous element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return teachers[int(current_index) - 1] # access the previous element
    except:
        return '' # return empty string in case of exception