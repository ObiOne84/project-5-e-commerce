# Generated by Django 3.2.24 on 2024-02-26 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_category_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subtitle',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
