# Generated by Django 5.0.6 on 2024-05-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_product_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_lifespan',
        ),
        migrations.AddField(
            model_name='product',
            name='product_discount_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]