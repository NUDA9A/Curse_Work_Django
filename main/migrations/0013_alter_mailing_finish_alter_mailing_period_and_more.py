# Generated by Django 5.0.4 on 2024-05-03 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_mailing_finish_alter_mailing_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 17, 7, 53, 212257, tzinfo=datetime.timezone.utc), verbose_name='дата и время окончания'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='period',
            field=models.CharField(choices=[('day', 'День'), ('week', 'Неделя'), ('month', 'Месяц')], default='День', max_length=30, verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 17, 7, 53, 212257, tzinfo=datetime.timezone.utc), verbose_name='дата и время начала'),
        ),
    ]
