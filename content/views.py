from django.shortcuts import render
from django.views.generic import ListView

from content.forms.contact_message_forms import ContactMessageForm
from content.models import Project, SkillCategory, Page


def index_view(request):
    context = {}
    form = ContactMessageForm
    projects = Project.objects.all()
    context['projects'] = projects
    context['pages'] = Page.objects.filter(show_on_homepage=True)
    context['skill_categories'] = SkillCategory.objects.all()
    context['form'] = form()
    return render(request, 'content/home.html', context=context)


def contact_message_form_view(request):
    context = {}

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactMessageForm()
            context['message'] = 'Your message was successfully sent'
        form = form
    else:
        form = ContactMessageForm()

    context['form'] = form

    if request.htmx:
        return render(request, template_name='content/partials/contact_message_form.html', context=context)
    return render(request, 'content/contact_message_form.html', context=context)


class ProjectListView(ListView):
    model = Project
    template_name_suffix = 's'
