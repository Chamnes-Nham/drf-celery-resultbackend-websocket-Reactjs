# Generated by Django 5.1.4 on 2025-01-14 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_alter_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
    ]
