# Generated by Django 5.0.4 on 2024-05-03 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0029_alter_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='booked_by',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='theater',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
    ]