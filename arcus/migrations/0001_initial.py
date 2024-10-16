# Generated by Django 5.0.7 on 2024-10-12 23:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created An')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=200, verbose_name='Project Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date')),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Paused', 'Paused'), ('Blocked', 'Blocked'), ('Waiting on Dependency', 'Waiting on Dependency')], default='Not Started', max_length=32, verbose_name='Status')),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=10, verbose_name='Priority')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_edited', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created An')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('title', models.CharField(max_length=200, verbose_name='Section Title')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_edited', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='arcus.project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
                'ordering': ['project', 'order'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created An')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=50, verbose_name='Tag Name')),
                ('color', models.CharField(default='#FFFFFF', max_length=7, verbose_name='Color')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_edited', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created An')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('title', models.CharField(max_length=200, verbose_name='Task Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Due Date')),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=10, verbose_name='Priority')),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Paused', 'Paused'), ('Blocked', 'Blocked'), ('Waiting on Dependency', 'Waiting on Dependency')], default='Not Started', max_length=32, verbose_name='Status')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Assigned To')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('dependencies', models.ManyToManyField(blank=True, related_name='dependent_tasks', to='arcus.task', verbose_name='Dependencies')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_edited', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
                ('parent_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='arcus.task', verbose_name='Parent Task')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='arcus.project', verbose_name='Project')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='arcus.section', verbose_name='Section')),
                ('tags', models.ManyToManyField(blank=True, related_name='tasks', to='arcus.tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['project', 'section', 'title'],
            },
        ),
    ]
