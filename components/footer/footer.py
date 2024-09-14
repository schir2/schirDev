from django_components import component

from content.models import Skill


@component.register("footer")
class Footer(component.Component):
    template_name = "template.html"

    def get_context_data(self):
        return {
            'skills': Skill.objects.all(),
        }

    class Media:
        css = "style.css"
