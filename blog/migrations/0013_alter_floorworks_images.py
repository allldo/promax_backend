# Generated by Django 4.2.16 on 2025-01-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_floorworksimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorworks',
            name='images',
            field=models.ManyToManyField(blank=True, to='blog.floorworksimage', verbose_name='Изображения'),
        ),
    ]
