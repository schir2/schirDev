# Generated by Django 5.0.7 on 2024-10-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcus', '0002_alter_project_creator_alter_project_editor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='starred',
            field=models.BooleanField(default=False, verbose_name='Starred'),
        ),
    ]
