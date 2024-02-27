# Generated by Django 3.2.24 on 2024-02-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_category_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='product_type',
            field=models.CharField(blank=True, choices=[('comic', 'Comic'), ('book', 'Book'), ('product', 'Product')], default=None, max_length=20, null=True),
        ),
    ]