# Generated by Django 5.0.7 on 2024-09-18 00:28

import content.storages
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_skillcategory_skill_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='skillcategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'Skill Categories'},
        ),
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.FileField(blank=True, null=True, storage=content.storages.OverwriteStorage(), upload_to='icons/', verbose_name='Icon'),
        ),
    ]
