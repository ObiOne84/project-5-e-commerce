# Generated by Django 3.2.24 on 2024-04-05 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_userprofile_default_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_full_name',
        ),
    ]
