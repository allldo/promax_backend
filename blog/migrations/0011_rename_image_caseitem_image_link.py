# Generated by Django 4.2.16 on 2025-01-28 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_caseitem_image_link_caseitem_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caseitem',
            old_name='image',
            new_name='image_link',
        ),
    ]
