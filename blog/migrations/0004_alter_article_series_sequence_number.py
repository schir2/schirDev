# Generated by Django 5.1.2 on 2024-11-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='series_sequence_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Series sequence number'),
        ),
    ]