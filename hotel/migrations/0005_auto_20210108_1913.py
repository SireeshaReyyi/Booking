# Generated by Django 3.1.4 on 2021-01-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20210108_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_room',
            name='booked',
        ),
        migrations.AddField(
            model_name='room_details',
            name='booked',
            field=models.BooleanField(default=True),
        ),
    ]
