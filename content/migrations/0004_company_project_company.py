# Generated by Django 5.0.7 on 2024-07-15 00:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_page_author_alter_page_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='content.company', verbose_name='Company'),
        ),
    ]