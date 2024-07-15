from django.urls import path, include

from content.views.home_views import home_view
from content.views.project_views import ProjectListView

app_name = 'content'

urlpatterns = [
    path('', home_view, name='home'),
    path('projects/', include([
        path('', ProjectListView.as_view(), name='project_list'),
    ]))
]
