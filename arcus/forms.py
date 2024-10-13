from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Project, Task, Tag, Section


# Project Form
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Enter project name')}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': _('Enter project description')}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(),
        }
        labels = {
            'name': _('Project Name'),
            'description': _('Description'),
            'start_date': _('Start Date'),
            'end_date': _('End Date'),
            'status': _('Status'),
        }
        help_texts = {
            'description': _('Provide a brief description of the project.'),
        }
        required = {
            'start_date': False,
            'end_date': False,
        }


# Task Form
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'status', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': _('Enter task title')}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': _('Enter task description')}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'priority': forms.Select(),
            'status': forms.Select(),
            'assigned_to': forms.Select(),
        }
        labels = {
            'title': _('Task Title'),
            'description': _('Description'),
            'due_date': _('Due Date'),
            'priority': _('Priority'),
            'status': _('Status'),
            'assigned_to': _('Assigned To'),
        }
        help_texts = {
            'description': _('Provide a brief description of the task.'),
        }
        required = {
            'due_date': False,
        }


# Tag Form
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Enter tag name')}),
            'color': forms.TextInput(attrs={'type': 'color'}),
        }
        labels = {
            'name': _('Tag Name'),
            'color': _('Color'),
        }


# Section Form
class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'order', 'project']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': _('Enter section title')}),
            'order': forms.NumberInput(attrs={'placeholder': _('Enter section order')}),
            'project': forms.Select(),
        }
        labels = {
            'title': _('Section Title'),
            'order': _('Order'),
            'project': _('Project'),
        }
        help_texts = {
            'title': _('Provide a title for the section.'),
            'order': _('Specify the order of the section within the project.'),
        }
