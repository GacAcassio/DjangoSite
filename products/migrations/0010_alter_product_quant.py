# Generated by Django 4.1.3 on 2022-12-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_quant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quant',
            field=models.IntegerField(default=0),
        ),
    ]