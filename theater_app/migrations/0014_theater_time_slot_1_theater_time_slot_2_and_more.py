# Generated by Django 5.0.4 on 2024-04-30 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0013_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='theater',
            name='time_slot_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='theater',
            name='time_slot_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='theater',
            name='time_slot_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='theater',
            name='time_slot_4',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
