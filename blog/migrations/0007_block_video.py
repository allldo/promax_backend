# Generated by Django 4.2.16 on 2025-01-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_block_title_alter_service_blocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='video',
            field=models.TextField(blank=True),
        ),
    ]
