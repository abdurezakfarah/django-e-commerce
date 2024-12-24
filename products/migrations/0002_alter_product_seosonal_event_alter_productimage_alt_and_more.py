# Generated by Django 5.1.4 on 2024-12-23 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seosonal_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.seosanalevents'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='alt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product_line',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.productline'),
        ),
    ]
