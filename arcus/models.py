from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_currentuser.db.models import CurrentUserField

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created An'))
    edited_at = models.DateTimeField(auto_now=True, verbose_name=_('Edited At'))
    creator = CurrentUserField(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_created', verbose_name=_('Creator'))
    editor = CurrentUserField(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_edited', verbose_name=_('Editor'))

    class Meta:
        abstract = True
        ordering = ['-created_at']


class StatusChoices(models.TextChoices):
    NOT_STARTED = 'Not Started', _('Not Started')
    IN_PROGRESS = 'In Progress', _('In Progress')
    COMPLETED = 'Completed', _('Completed')
    PAUSED = 'Paused', _('Paused')
    BLOCKED = 'Blocked', _('Blocked')
    WAITING = 'Waiting on Dependency', _('Waiting on Dependency')


class PriorityChoices(models.TextChoices):
    HIGH = 'High', _('High')
    MEDIUM = 'Medium', _('Medium')
    LOW = 'Low', _('Low')


class Project(BaseModel):
    """
    Represents a project that contains multiple tasks and sections.
    """
    name = models.CharField(max_length=200, verbose_name=_('Project Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    start_date = models.DateTimeField(null=True, blank=True, verbose_name=_('Start Date'))
    end_date = models.DateTimeField(null=True, blank=True, verbose_name=_('End Date'))
    status = models.CharField(max_length=32, choices=StatusChoices.choices, default=StatusChoices.NOT_STARTED, verbose_name=_('Status'))
    priority = models.CharField(max_length=10, choices=PriorityChoices.choices, default=PriorityChoices.MEDIUM, verbose_name=_('Priority'))

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ['name']

    def __str__(self):
        return self.name


class Section(BaseModel):
    """
    Represents a section within a project used to group tasks.
    """
    title = models.CharField(max_length=200, verbose_name=_('Section Title'))
    order = models.IntegerField(default=0, verbose_name=_('Order'))
    project = models.ForeignKey(Project, related_name='sections', on_delete=models.CASCADE, verbose_name=_('Project'))

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ['project', 'order']

    def __str__(self):
        return f"{self.project.name} - {self.title}"


class Task(BaseModel):
    """
    Represents a task, which may belong to a project and optionally to a section.
    """
    title = models.CharField(max_length=200, verbose_name=_('Task Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    due_date = models.DateTimeField(null=True, blank=True, verbose_name=_('Due Date'))
    priority = models.CharField(max_length=10, choices=PriorityChoices.choices, default=PriorityChoices.MEDIUM, verbose_name=_('Priority'))
    status = models.CharField(max_length=32, choices=StatusChoices.choices, default=StatusChoices.NOT_STARTED, verbose_name=_('Status'))
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks',
                                    verbose_name=_('Assigned To'))
    tags = models.ManyToManyField('Tag', related_name='tasks', blank=True, verbose_name=_('Tags'))
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subtasks',
                                    verbose_name=_('Parent Task'))
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE, verbose_name=_('Project'))
    section = models.ForeignKey(Section, null=True, blank=True, related_name='tasks', on_delete=models.CASCADE, verbose_name=_('Section'))
    dependencies = models.ManyToManyField('self', symmetrical=False, related_name='dependent_tasks', blank=True,
                                          verbose_name=_('Dependencies'))

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
        ordering = ['project', 'section', 'title']

    def __str__(self):
        return self.title


class Tag(BaseModel):
    """
    Represents a tag that can be assigned to tasks for categorization.
    """
    name = models.CharField(max_length=50, verbose_name=_('Tag Name'))
    color = models.CharField(max_length=7, default='#FFFFFF', verbose_name=_('Color'))  # Default to white

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        ordering = ['name']

    def __str__(self):
        return self.name
