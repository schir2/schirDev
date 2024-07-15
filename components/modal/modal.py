from django_components import component


@component.register("modal")
class Modal(component.Component):
    template_name = "template.html"

    def get_context_data(self, title: str, text: str, id: str, open_button_text='Open'):
        return {
            'title': title,
            'text': text,
            'id': id,
            'open_button_text': open_button_text,
        }

    class Media:
        css = "style.css"
