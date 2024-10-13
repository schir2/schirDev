from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from arcus.models import Task
from arcus.forms import TaskForm
from arcus.filters import TaskFilter


# Task List View
def task_list_view(request):
    context = {}
    task_filter = TaskFilter(request.GET, queryset=Task.objects.all().order_by('due_date'))
    context['filter'] = task_filter
    context['tasks'] = task_filter.qs

    if request.htmx:
        return render(request, 'arcus/partials/task_list_partial.html', context)
    return render(request, 'arcus/pages/task_list.html', context)


# Task Detail View
def task_detail_view(request, pk):
    context = {}
    task = get_object_or_404(Task, pk=pk)
    context['task'] = task

    if request.htmx:
        return render(request, 'arcus/partials/task_detail_partial.html', context)
    return render(request, 'arcus/pages/task_detail.html', context)


# Task Create View
def task_create_view(request):
    context = {}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            if request.htmx:
                return render(request, 'arcus/partials/task_card.html', {'task': task})
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()

    context['form'] = form
    if request.htmx:
        return render(request, 'arcus/partials/task_form_partial.html', context)
    return render(request, 'arcus/forms/task_form.html', context)


# Task Edit View
def task_edit_view(request, pk):
    context = {}
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            if request.htmx:
                return render(request, 'arcus/partials/task_card.html', {'task': task})
            return redirect('task_detail', pk=pk)
    else:
        form = TaskForm(instance=task)

    context['form'] = form
    if request.htmx:
        return render(request, 'arcus/partials/task_form_partial.html', context)
    return render(request, 'arcus/forms/task_form.html', context)


# Task Delete View
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        if request.htmx:
            return JsonResponse({'success': True})
        return redirect('task_list')

    return render(request, 'arcus/partials/task_confirm_delete.html', {'task': task})