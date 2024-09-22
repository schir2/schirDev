# Generated by Django 5.0.7 on 2024-09-22 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='show_in_navbar',
            field=models.BooleanField(default=False, verbose_name='Show on navigation'),
        ),
        migrations.AddField(
            model_name='page',
            name='show_on_homepage',
            field=models.BooleanField(default=False, verbose_name='Show on homepage'),
        ),
    ]