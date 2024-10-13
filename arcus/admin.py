from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Project, Section, Task, Tag


@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('name', 'status', 'priority', 'start_date', 'end_date', 'created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('status', 'priority', 'start_date', 'end_date')
    search_fields = ('name', 'description')
    ordering = ('name', 'start_date')
    readonly_fields = ('created_at', 'edited_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'start_date', 'end_date', 'status', 'priority')
        }),
        ('Metadata', {
            'fields': ('created_at', 'edited_at', 'creator', 'editor')
        }),
    )


@admin.register(Section)
class SectionAdmin(ImportExportModelAdmin):
    list_display = ('title', 'project', 'order', 'created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('project',)
    search_fields = ('title', 'project__name')
    ordering = ('project', 'order')
    readonly_fields = ('created_at', 'edited_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'project', 'order')
        }),
        ('Metadata', {
            'fields': ('created_at', 'edited_at', 'creator', 'editor')
        }),
    )


@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    list_display = (
    'title', 'project', 'section', 'status', 'priority', 'due_date', 'assigned_to', 'created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('status', 'priority', 'project', 'section', 'due_date')
    search_fields = ('title', 'description', 'project__name', 'section__title', 'assigned_to__username')
    ordering = ('project', 'section', 'title')
    readonly_fields = ('created_at', 'edited_at')
    filter_horizontal = ('tags', 'dependencies')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'section', 'due_date', 'status', 'priority', 'assigned_to', 'parent_task', 'tags',
                       'dependencies')
        }),
        ('Metadata', {
            'fields': ('created_at', 'edited_at', 'creator', 'editor')
        }),
    )


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name', 'color', 'created_at', 'edited_at', 'creator', 'editor')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'edited_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'color')
        }),
        ('Metadata', {
            'fields': ('created_at', 'edited_at', 'creator', 'editor')
        }),
    )
