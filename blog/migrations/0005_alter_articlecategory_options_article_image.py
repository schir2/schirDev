# Generated by Django 5.0.7 on 2024-09-26 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_content_alter_comment_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['name'], 'verbose_name': 'Article Category', 'verbose_name_plural': 'Article Categories'},
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/article_images/', verbose_name='Image'),
        ),
    ]