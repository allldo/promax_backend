# Generated by Django 4.2.16 on 2024-11-02 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_product_slug'),
        ('blog', '0010_floorworkitem_floorworks_advantage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advantage',
            name='image',
        ),
        migrations.AddField(
            model_name='advantage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.image'),
        ),
    ]
