# Generated by Django 4.2.3 on 2023-09-08 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacker_news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authpermission',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='authpermission',
            name='custom_user',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
    ]