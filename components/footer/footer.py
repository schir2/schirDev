from django_components import component

from content.models import TechStack


@component.register("footer")
class Footer(component.Component):
    template_name = "template.html"

    def get_context_data(self):
        return {
            'tech_stacks': TechStack.objects.all(),
        }

    class Media:
        css = "style.css"
