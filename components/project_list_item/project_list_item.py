from django_components import component


@component.register("project_list_item")
class ProjectListItem(component.Component):
    template_name = "template.html"

    def get_context_data(self, project):
        return {
            "project": project,
        }

    class Media:
        css = "style.css"
