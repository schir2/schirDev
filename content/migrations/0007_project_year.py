# Generated by Django 5.0.7 on 2024-07-15 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_alter_techstack_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.PositiveSmallIntegerField(default=2024, verbose_name='Year'),
        ),
    ]
