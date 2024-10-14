from django.urls import path, include

from .views import (
    project_list_view, project_detail_view, project_create_view, project_edit_view, project_delete_view,
    task_list_view, task_detail_view, task_create_view, task_edit_view, task_delete_view,
    tag_list_view, tag_detail_view, tag_create_view, tag_edit_view, tag_delete_view,
    section_list_view, section_detail_view, section_create_view, section_edit_view, section_delete_view, index_view,
    project_toggle_star, project_starred_list_sidenav
)

app_name = 'arcus'

project_patterns = ([
    path('', project_list_view, name='project_list'),
    path('project_starred_list_sidenav', project_starred_list_sidenav, name='project_starred_list_sidenav'),
    path('create/', project_create_view, name='project_create'),
    path('<int:pk>/', include([
        path('', project_detail_view, name='project_detail'),
        path('edit/', project_edit_view, name='project_edit'),
        path('star/', project_toggle_star, name='project_toggle_star'),

        path('delete/', project_delete_view, name='project_delete'),
    ])),
])

task_patterns = ([
    path('', task_list_view, name='task_list'),
    path('create/', task_create_view, name='task_create'),
    path('<int:pk>/', include([
        path('', task_detail_view, name='task_detail'),
        path('edit/', task_edit_view, name='task_edit'),
        path('delete/', task_delete_view, name='task_delete'),
    ])),
])

tag_patterns = ([
    path('', tag_list_view, name='tag_list'),
    path('create/', tag_create_view, name='tag_create'),
    path('<int:pk>/', include([
        path('', tag_detail_view, name='tag_detail'),
        path('edit/', tag_edit_view, name='tag_edit'),
        path('delete/', tag_delete_view, name='tag_delete'),
    ])),
])

section_patterns = ([
    path('', section_list_view, name='section_list'),
    path('create/', section_create_view, name='section_create'),
    path('<int:pk>/', include([
        path('', section_detail_view, name='section_detail'),
        path('edit/', section_edit_view, name='section_edit'),
        path('delete/', section_delete_view, name='section_delete'),
    ])),
])

urlpatterns = [
    path('', index_view, name='index'),
    path('projects/', include(project_patterns)),
    path('tasks/', include(task_patterns)),
    path('tags/', include(tag_patterns)),
    path('sections/', include(section_patterns)),
]
