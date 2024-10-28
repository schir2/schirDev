# Generated by Django 5.0.7 on 2024-10-27 18:28

import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_article_content_alter_comment_content'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='article',
            name='series_sequence_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Series sequence number'),
        ),
        migrations.CreateModel(
            name='ArticleSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Article Series',
                'verbose_name_plural': 'Article Series',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='blog.articleseries', verbose_name='Series'),
        ),
        migrations.AddConstraint(
            model_name='article',
            constraint=models.UniqueConstraint(fields=('title', 'creator'), name='unique_title_creator'),
        ),
        migrations.AddConstraint(
            model_name='article',
            constraint=models.UniqueConstraint(fields=('series', 'series_sequence_number'), name='unique_series_sequence_number'),
        ),
    ]
