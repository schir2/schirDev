from django.views.generic import ListView

from content.models import Project


class ProjectListView(ListView):
    model = Project
    template_name_suffix = '_list'
