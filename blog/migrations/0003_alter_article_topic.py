# Generated by Django 5.1.2 on 2024-11-01 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='blog.topic', verbose_name='Topic'),
        ),
    ]
