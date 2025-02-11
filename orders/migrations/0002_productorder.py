# Generated by Django 4.2.16 on 2024-11-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField()),
                ('delivery_on_order', models.TextField()),
                ('comments_on_order', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_items', models.ManyToManyField(blank=True, to='shop.product')),
            ],
        ),
    ]
