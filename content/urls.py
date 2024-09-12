from django.urls import path, include

from content.views import home_view, about_view, bio_view, resume_view, contact_view, ProjectListView

app_name = 'content'

urlpatterns = [
    path('', home_view, name='home'),
    path('about', about_view, name='about'),
    path('bio', bio_view, name='bio'),
    path('contact', contact_view, name='contact'),
    path('resume', resume_view, name='resume'),
    path('projects/', include([
        path('', ProjectListView.as_view(), name='project_list'),
    ]))
]
