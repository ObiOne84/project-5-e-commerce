# Generated by Django 3.2.24 on 2024-03-25 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='order',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]