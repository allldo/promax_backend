# Generated by Django 4.2.16 on 2024-10-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_caseitem_link_caseitem_iframe'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='subtitle',
            field=models.CharField(default='subtitle', max_length=275),
            preserve_default=False,
        ),
    ]