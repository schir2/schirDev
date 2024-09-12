from django.shortcuts import render
from django.views.generic import ListView

from content.models import Project


def home_view(request):
    context = {}
    projects = Project.objects.all()
    context['projects'] = projects
    return render(request, 'content/home.html', context=context)


def about_view(request):
    return render(request, 'content/about.html')


def bio_view(request):
    return render(request, 'content/bio.html')


def resume_view(request):
    return render(request, 'content/resume.html')


def contact_view(request):
    return render(request, 'content/contact.html')


class ProjectListView(ListView):
    model = Project
    template_name_suffix = 's'
