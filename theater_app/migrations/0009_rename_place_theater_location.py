# Generated by Django 5.0.4 on 2024-04-25 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0008_theater'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theater',
            old_name='place',
            new_name='location',
        ),
    ]
