from django.urls import path, include

from .views import (
    project_list_view, project_detail_view, project_create_view, project_edit_view, project_delete_view,
    task_list_view, task_detail_view, task_create_view, task_edit_view, task_delete_view,
    tag_list_view, tag_detail_view, tag_create_view, tag_edit_view, tag_delete_view,
    section_list_view, section_detail_view, section_create_view, section_edit_view, section_delete_view
)

project_patterns = ([
    path('', project_list_view, name='project_list'),
    path('create/', project_create_view, name='create_project'),
    path('<int:pk>/', include([
        path('', project_detail_view, name='project_detail'),
        path('edit/', project_edit_view, name='edit_project'),
        path('delete/', project_delete_view, name='delete_project'),
    ])),
], 'project')

task_patterns = ([
    path('', task_list_view, name='task_list'),
    path('create/', task_create_view, name='create_task'),
    path('<int:pk>/', include([
        path('', task_detail_view, name='task_detail'),
        path('edit/', task_edit_view, name='edit_task'),
        path('delete/', task_delete_view, name='delete_task'),
    ])),
], 'task')

tag_patterns = ([
    path('', tag_list_view, name='tag_list'),
    path('create/', tag_create_view, name='create_tag'),
    path('<int:pk>/', include([
        path('', tag_detail_view, name='tag_detail'),
        path('edit/', tag_edit_view, name='edit_tag'),
        path('delete/', tag_delete_view, name='delete_tag'),
    ])),
], 'tag')

section_patterns = ([
    path('', section_list_view, name='section_list'),
    path('create/', section_create_view, name='create_section'),
    path('<int:pk>/', include([
        path('', section_detail_view, name='section_detail'),
        path('edit/', section_edit_view, name='edit_section'),
        path('delete/', section_delete_view, name='delete_section'),
    ])),
], 'section')

urlpatterns = [
    path('projects/', include((project_patterns, 'projects'))),
    path('tasks/', include((task_patterns, 'tasks'))),
    path('tags/', include((tag_patterns, 'tags'))),
    path('sections/', include((section_patterns, 'sections'))),
]
