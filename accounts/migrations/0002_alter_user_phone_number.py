# Generated by Django 5.0.6 on 2024-05-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, unique=True, verbose_name='phone number'),
        ),
    ]
