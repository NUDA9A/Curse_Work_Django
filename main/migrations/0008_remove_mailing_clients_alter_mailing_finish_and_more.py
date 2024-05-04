# Generated by Django 5.0.4 on 2024-05-03 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_mailing_finish_alter_mailing_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='clients',
        ),
        migrations.AlterField(
            model_name='mailing',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 16, 52, 23, 395832, tzinfo=datetime.timezone.utc), verbose_name='дата и время окончания'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 16, 52, 23, 395832, tzinfo=datetime.timezone.utc), verbose_name='дата и время начала'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='clients',
            field=models.ManyToManyField(blank=True, null=True, to='main.client'),
        ),
    ]
