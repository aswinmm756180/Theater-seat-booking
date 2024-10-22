# Generated by Django 5.0.4 on 2024-05-03 06:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0033_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='theater_app.movie'),
        ),
        migrations.AddField(
            model_name='booking',
            name='theater',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='theater_app.theater'),
        ),
        migrations.AddField(
            model_name='booking',
            name='time_slot',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seats_booked',
            field=models.ManyToManyField(blank=True, null=True, related_name='bookings', to='theater_app.seat'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
