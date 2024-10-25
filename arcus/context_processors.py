from .models import Project


def starred_projects(request):
    return {'starred_projects': Project.objects.filter(starred=True)}
