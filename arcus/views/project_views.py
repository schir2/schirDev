from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django_htmx.http import trigger_client_event

from arcus.filters import ProjectFilter
from arcus.forms import ProjectForm
from arcus.models import Project


# Project Create View
def project_create_view(request):
    context = {}
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            if request.htmx:
                return render(request, 'arcus/partials/project_card.html', {'project': project})
            return redirect('project_detail_view', pk=project.pk)
    else:
        form = ProjectForm()

    context['form'] = form
    if request.htmx:
        return render(request, 'arcus/partials/project_form_partial.html', context)
    return render(request, 'arcus/forms/project_form.html', context)


# Project List View
def project_list_view(request):
    context = {}
    project_filter = ProjectFilter(request.GET, queryset=Project.objects.all().order_by('start_date'))
    context['filter'] = project_filter
    context['projects'] = project_filter.qs

    if request.htmx:
        return render(request, 'arcus/partials/project_list_partial.html', context)
    return render(request, 'arcus/pages/project_list.html', context)


# Project Detail View
def project_detail_view(request, pk):
    context = {}
    project = get_object_or_404(Project, pk=pk)
    context['project'] = project

    if request.htmx:
        return render(request, 'arcus/partials/project_detail_partial.html', context)
    return render(request, 'arcus/pages/project_detail.html', context)


# Project Edit View
def project_edit_view(request, pk):
    context = {}
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            if request.htmx:
                return render(request, 'arcus/partials/project_detail_partial.html', {'project': project})
            return redirect('project_detail', pk=pk)
    else:
        form = ProjectForm(instance=project)

    context['form'] = form
    if request.htmx:
        return render(request, 'arcus/partials/project_form_partial.html', context)
    return render(request, 'arcus/forms/project_form.html', context)


# Project Delete View
def project_delete_view(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project.delete()
        if request.htmx:
            return JsonResponse({'success': True})
        return redirect('project_list')

    return render(request, 'arcus/partials/project_confirm_delete.html', {'project': project})


@login_required
@require_POST
def project_toggle_star(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.starred = not project.starred
    project.save()
    response = render(request, 'arcus/partials/project_star_button.html', {'project': project})
    trigger_client_event(response, 'project_star_toggle')
    return response


def project_starred_list_sidenav(request):
    starred_projects = Project.objects.filter(starred=True)
    context = {'starred_projects': starred_projects}
    return render(request, template_name='arcus/partials/project_list_sidenav.html', context=context)
