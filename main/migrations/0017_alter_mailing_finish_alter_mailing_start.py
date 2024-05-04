# Generated by Django 5.0.4 on 2024-05-03 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_mailing_clients_alter_mailing_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 17, 57, 43, 806440, tzinfo=datetime.timezone.utc), verbose_name='дата и время окончания'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 17, 57, 43, 806440, tzinfo=datetime.timezone.utc), verbose_name='дата и время начала'),
        ),
    ]
