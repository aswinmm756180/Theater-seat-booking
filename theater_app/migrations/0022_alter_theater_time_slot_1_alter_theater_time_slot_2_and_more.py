# Generated by Django 5.0.4 on 2024-04-30 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0021_alter_theater_time_slot_1_alter_theater_time_slot_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='time_slot_1',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='theater',
            name='time_slot_2',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='theater',
            name='time_slot_3',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='theater',
            name='time_slot_4',
            field=models.TimeField(blank=True, null=True),
        ),
    ]