# Generated by Django 3.2.24 on 2024-03-06 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_rename_ave_rating_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=19, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
    ]