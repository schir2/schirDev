from django_components import component


@component.register("card")
class Card(component.Component):
    template_name = "template.html"

    def get_context_data(self, title: str, text: str = ""):
        return {
            'title': title,
            'text': text,
        }

    class Media:
        css = "style.css"
