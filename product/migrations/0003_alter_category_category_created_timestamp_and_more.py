# Generated by Django 5.0.6 on 2024-05-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_category_image_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_created_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_updated_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_created_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_updated_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
