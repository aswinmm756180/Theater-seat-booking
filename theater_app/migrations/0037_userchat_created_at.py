# Generated by Django 5.0.6 on 2024-05-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0036_userchat'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]