# Generated by Django 5.0.4 on 2024-05-03 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_mailing_finish_alter_mailing_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='clients',
            field=models.ManyToManyField(blank=True, null=True, to='main.client', verbose_name='Клиенты'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 17, 35, 9, 112772, tzinfo=datetime.timezone.utc), verbose_name='дата и время окончания'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 17, 35, 9, 112772, tzinfo=datetime.timezone.utc), verbose_name='дата и время начала'),
        ),
    ]
