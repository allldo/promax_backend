# Generated by Django 4.2.16 on 2025-01-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_caseitem_link_alter_caseitem_iframe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caseitem',
            old_name='link',
            new_name='image_link',
        ),
        migrations.AddField(
            model_name='caseitem',
            name='post_link',
            field=models.TextField(blank=True),
        ),
    ]
