# Generated by Django 4.2.9 on 2024-02-11 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_image_image_alter_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
    ]
