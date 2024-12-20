from django.contrib.auth.decorators import login_not_required
from django.shortcuts import render
from django.utils import timezone

from arcus.models import Project, Task


@login_not_required
def index_view(request):
    context = {}
    # Get the recent projects and tasks
    recent_projects = Project.objects.order_by('-created_at')[:5]
    starred_projects = Project.objects.filter(starred=True)[:5]
    recent_tasks = Task.objects.order_by('-created_at')[:5]

    # Collect overall statistics
    total_projects = Project.objects.count()
    total_tasks = Task.objects.count()
    tasks_in_progress = Task.objects.filter(status='In Progress').count()
    overdue_tasks = Task.objects.filter(status='Not Started', due_date__lt=timezone.now()).count()

    # Add data to the context
    context['recent_projects'] = recent_projects
    context['starred_projects'] = starred_projects
    context['recent_tasks'] = recent_tasks
    context['total_projects'] = total_projects
    context['total_tasks'] = total_tasks
    context['tasks_in_progress'] = tasks_in_progress
    context['overdue_tasks'] = overdue_tasks

    return render(request, 'arcus/pages/index.html', context)
