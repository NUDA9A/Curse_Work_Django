# Generated by Django 5.0.4 on 2024-05-03 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_mailing_finish_alter_mailing_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='next_sending_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время следующей рассылки'),
        ),
        migrations.AddField(
            model_name='try',
            name='status',
            field=models.BooleanField(blank=True, null=True, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 23, 13, 46, 530360, tzinfo=datetime.timezone.utc), verbose_name='дата и время окончания'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 23, 13, 46, 530360, tzinfo=datetime.timezone.utc), verbose_name='дата и время начала'),
        ),
        migrations.AlterField(
            model_name='try',
            name='last_try',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='последняя попытка'),
        ),
    ]
