# Generated by Django 5.1.4 on 2025-01-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0005_product_deal_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='company')),
            ],
        ),
    ]
