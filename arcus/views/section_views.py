from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from arcus.models import Section
from arcus.forms import SectionForm
from arcus.filters import SectionFilter


# Section List View
def section_list_view(request):
    context = {}
    section_filter = SectionFilter(request.GET, queryset=Section.objects.all().order_by('title'))
    context['filter'] = section_filter
    context['sections'] = section_filter.qs

    if request.htmx:
        return render(request, 'arcus/partials/section_list_partial.html', context)
    return render(request, 'arcus/pages/section_list.html', context)


# Section Detail View
def section_detail_view(request, pk):
    context = {}
    section = get_object_or_404(Section, pk=pk)
    context['section'] = section

    if request.htmx:
        return render(request, 'arcus/partials/section_detail_partial.html', context)
    return render(request, 'arcus/pages/section_detail.html', context)


# Section Create View
def section_create_view(request):
    context = {}
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save()
            if request.htmx:
                return render(request, 'arcus/partials/section_card.html', {'section': section})
            return redirect('section_detail_view', pk=section.pk)
    else:
        form = SectionForm()

    context['form'] = form
    if request.htmx:
        return render(request, 'arcus/partials/section_form_partial.html', context)
    return render(request, 'arcus/forms/section_form.html', context)


# Section Edit View
def section_edit_view(request, pk):
    context = {}
    section = get_object_or_404(Section, pk=pk)

    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            section = form.save()
            if request.htmx:
                return render(request, 'arcus/partials/section_card.html', {'section': section})
            return redirect('section_detail_view', pk=pk)
    else:
        form = SectionForm(instance=section)

    context['form'] = form
    if request.htmx:
        return render(request, 'arcus/partials/section_form_partial.html', context)
    return render(request, 'arcus/forms/section_form.html', context)


# Section Delete View
def section_delete_view(request, pk):
    section = get_object_or_404(Section, pk=pk)

    if request.method == 'POST':
        section.delete()
        if request.htmx:
            return JsonResponse({'success': True})
        return redirect('section_list_view')

    return render(request, 'arcus/partials/section_confirm_delete.html', {'section': section})