# Generated by Django 4.0.4 on 2022-05-24 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_posts_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=3000, null=True),
        ),
    ]
