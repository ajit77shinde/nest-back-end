# Generated by Django 5.0.6 on 2024-05-15 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
                ('category_image_url', models.URLField(default='abs')),
                ('category_is_active', models.BooleanField(default=True)),
                ('category_created_by', models.CharField(max_length=255)),
                ('category_updated_by', models.CharField(max_length=255)),
                ('category_created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('category_updated_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_tag', models.CharField(choices=[('SALE', 'Sale'), ('NEW', 'New'), ('HOT', 'Hot'), ('DISCOUNT', 'Discount')], default='NEW', max_length=255)),
                ('product_seller_name', models.CharField(max_length=255)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_discount_percent', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('product_image_url', models.URLField(default='abs')),
                ('product_description', models.TextField()),
                ('product_manufacturing_date', models.DateField()),
                ('product_stocks_left', models.IntegerField()),
                ('product_is_active', models.BooleanField(default=True)),
                ('product_created_by', models.CharField(max_length=255)),
                ('product_updated_by', models.CharField(max_length=255)),
                ('product_created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('product_updated_timestamp', models.DateTimeField(auto_now_add=True)),
                ('product_category', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
