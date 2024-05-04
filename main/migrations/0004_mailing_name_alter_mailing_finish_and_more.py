# Generated by Django 5.0.4 on 2024-05-03 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_mailing_finish_alter_mailing_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 16, 31, 42, 112436, tzinfo=datetime.timezone.utc), verbose_name='дата и время окончания'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 16, 31, 42, 112436, tzinfo=datetime.timezone.utc), verbose_name='дата и время начала'),
        ),
    ]