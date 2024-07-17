from django.urls import reverse
from django_components import component

from content.utils.get_active_link_class import get_active_link_class


@component.register("link")
class Link(component.Component):
    template_name = "template.html"

    def get_context_data(self, href: str = '', url: str = None):
        request = self.outer_context.get('request')
        href = reverse(url) if url else href

        active_link_class = get_active_link_class(href, request)

        return {
            'href': href,
            'active_link_class': active_link_class
        }

    class Media:
        css = "style.css"
