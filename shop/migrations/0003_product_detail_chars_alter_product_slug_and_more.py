# Generated by Django 4.2.16 on 2024-10-26 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_image_service_product_sale_remove_product_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail_chars',
            field=models.JSONField(default={'q': 1}),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='shop.category'),
        ),
    ]