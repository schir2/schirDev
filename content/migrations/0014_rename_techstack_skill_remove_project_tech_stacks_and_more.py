# Generated by Django 5.0.7 on 2024-09-14 22:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_techstack_proficiency'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TechStack',
            new_name='Skill',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tech_stacks',
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(related_name='projects', to='content.skill', verbose_name='Skills'),
        ),
    ]
