# Generated by Django 3.2.24 on 2024-03-08 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
    ]
