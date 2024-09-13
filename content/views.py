from django.shortcuts import render
from django.views.generic import ListView

from content.forms.contact_message_forms import ContactMessageForm
from content.models import Project


def home_view(request):
    context = {}
    form = ContactMessageForm
    projects = Project.objects.all()
    context['projects'] = projects
    context['form'] = form()
    return render(request, 'content/home.html', context=context)


def contact_message_form_view(request):
    context = {}
    form = ContactMessageForm
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
        context['form'] = form
    else:
        context['form'] = form()
    return render(request, 'content/home.html', context=context)


class ProjectListView(ListView):
    model = Project
    template_name_suffix = 's'
