# Generated by Django 5.0.4 on 2024-05-01 09:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0026_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='booked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='seat',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_seats', to='theater_app.movie'),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
