# Generated by Django 4.2.16 on 2024-10-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parketnaya_himia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sposob_ukladki',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]