# Generated by Django 5.0.4 on 2024-05-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0028_alter_seat_booked_by_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
    ]