# Project Filter
import django_filters
from django.utils.translation import gettext_lazy as _

from arcus.models import Task, Tag, Project, Section


# Project Filter
class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label=_('Name'))
    status = django_filters.ChoiceFilter(choices=Project._meta.get_field('status').choices, label=_('Status'))
    priority = django_filters.ChoiceFilter(choices=Project._meta.get_field('priority').choices, label=_('Priority'))
    start_date = django_filters.DateFromToRangeFilter(label=_('Start Date Range'))

    class Meta:
        model = Project
        fields = ['name', 'status', 'priority', 'start_date']


# Task Filter
class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label=_('Title'))
    priority = django_filters.ChoiceFilter(choices=Task._meta.get_field('priority').choices, label=_('Priority'))
    status = django_filters.ChoiceFilter(choices=Task._meta.get_field('status').choices, label=_('Status'))
    due_date = django_filters.DateFromToRangeFilter(label=_('Due Date Range'))

    class Meta:
        model = Task
        fields = ['title', 'priority', 'status', 'due_date']


# Tag Filter
class TagFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label=_('Name'))

    class Meta:
        model = Tag
        fields = ['name']


# Section Filter
class SectionFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label=_('Title'))
    project = django_filters.CharFilter(lookup_expr='icontains', label=_('Project'))

    class Meta:
        model = Section
        fields = ['title', 'project']
