# Generated by Django 5.0.7 on 2024-07-15 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_company_project_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='techstack',
            options={'ordering': ['name']},
        ),
    ]