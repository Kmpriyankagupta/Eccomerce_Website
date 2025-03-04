# Generated by Django 5.1.4 on 2025-01-25 09:47

import django.contrib.postgres.fields
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
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='category')),
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
            name='register_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=100)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='company')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.BigIntegerField(default=0)),
                ('price_caption', models.CharField(max_length=10)),
                ('rateing', models.FloatField(default=2)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='product_image')),
                ('deal_price', models.BigIntegerField(default=10000)),
                ('sizes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=9), blank=True, default=list, size=None)),
                ('colors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=9), blank=True, default=list, size=None)),
                ('sort_des', models.CharField(blank=True, max_length=100, null=True)),
                ('long_des', models.CharField(blank=True, max_length=500, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.categories')),
            ],
        ),
    ]
