from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from arcus.models import Tag
from arcus.forms import TagForm
from arcus.filters import TagFilter


# Tag List View
def tag_list_view(request):
    context = {}
    tag_filter = TagFilter(request.GET, queryset=Tag.objects.all().order_by('name'))
    context['filter'] = tag_filter
    context['tags'] = tag_filter.qs

    if request.htmx:
        return render(request, 'arcus/partials/tag_list_partial.html', context)
    return render(request, 'arcus/pages/tag_list.html', context)


# Tag Detail View
def tag_detail_view(request, pk):
    context = {}
    tag = get_object_or_404(Tag, pk=pk)
    context['tag'] = tag

    if request.htmx:
        return render(request, 'arcus/partials/tag_detail_partial.html', context)
    return render(request, 'arcus/pages/tag_detail.html', context)


# Tag Create View
def tag_create_view(request):
    context = {}
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            if request.htmx:
                return render(request, 'arcus/partials/tag_card.html', {'tag': tag})
            return redirect('tag_detail_view', pk=tag.pk)
    else:
        form = TagForm()

    context['form'] = form
    if request.htmx:
        return render(request, 'arcus/partials/tag_form_partial.html', context)
    return render(request, 'arcus/forms/tag_form.html', context)


# Tag Edit View
def tag_edit_view(request, pk):
    context = {}
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save()
            if request.htmx:
                return render(request, 'arcus/partials/tag_card.html', {'tag': tag})
            return redirect('tag_detail_view', pk=pk)
    else:
        form = TagForm(instance=tag)

    context['form'] = form
    if request.htmx:
        return render(request, 'arcus/partials/tag_form_partial.html', context)
    return render(request, 'arcus/forms/tag_form.html', context)


# Tag Delete View
def tag_delete_view(request, pk):
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == 'POST':
        tag.delete()
        if request.htmx:
            return JsonResponse({'success': True})
        return redirect('tag_list_view')

    return render(request, 'arcus/partials/tag_confirm_delete.html', {'tag': tag})