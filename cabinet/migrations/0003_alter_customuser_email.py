# Generated by Django 4.2.16 on 2024-11-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0002_customuser_favorite_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
