# Generated by Django 5.1.4 on 2025-01-09 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='highlightdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mainimage')),
                ('image_title', models.CharField(max_length=50)),
                ('image_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_offer_image', models.ImageField(upload_to='offerimage')),
                ('special_offer_title', models.CharField(max_length=50)),
                ('special_offer_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.BigIntegerField(default=0)),
                ('price_caption', models.CharField(max_length=10)),
                ('rateing', models.IntegerField(default=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.categories')),
            ],
        ),
    ]
