from django.db.models import Q

from content.models import Page


def navbar_items(request):
    return {'navbar_items': get_navbar_items}


def get_navbar_items():
    navbar_items = Page.objects.filter(Q(show_in_navbar=True) | Q(show_on_homepage=True))
    return navbar_items
