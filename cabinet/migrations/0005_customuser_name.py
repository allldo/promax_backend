# Generated by Django 4.2.16 on 2024-11-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0004_remove_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
