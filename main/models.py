import datetime

import pytz
from django.conf import settings
from django.db import models

from config.settings import AUTH_USER_MODEL

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(verbose_name="контактная почта", **NULLABLE)
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    comment = models.CharField(max_length=150, verbose_name="Комментарий", **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name="Владелец", **NULLABLE)

    def __str__(self):
        return f"ФИО: {self.full_name}, Email: {self.email}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Message(models.Model):
    header = models.CharField(max_length=150, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст сообщения")
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name="Владелец", **NULLABLE)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Mailing(models.Model):
    zone = pytz.timezone(settings.TIME_ZONE)
    current_time = datetime.datetime.now(zone)
    name = models.CharField(max_length=100, verbose_name="Название рассылки", **NULLABLE)
    date_time = models.DateTimeField(default=current_time, verbose_name="Дата и время первой рассылки")
    period_choices = {"День": "day", "Неделя": "week", "Месяц": "month"}
    period = models.CharField(max_length=30, choices=period_choices, default="День", verbose_name="периодичность")
    status_choices = {"Создана": "created", "Выполняется": "ongoing", "Завершена": "finished"}
    status = models.CharField(max_length=30, choices=status_choices, default="Создана", verbose_name="статус рассылки")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="сообщение", **NULLABLE)
    clients = models.ManyToManyField(Client, verbose_name="Клиенты", **NULLABLE)
    start = models.DateTimeField(default=current_time, verbose_name="дата и время начала")
    finish = models.DateTimeField(default=current_time + datetime.timedelta(days=30),
                                  verbose_name="дата и время окончания")
    is_active = models.BooleanField(default=False, verbose_name="активность")
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name="Владелец", **NULLABLE)
    next_sending_time = models.DateTimeField(verbose_name="Время следующей рассылки", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ("set_active", "Can set is_active"),
        ]


class Try(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="рассылка")
    last_try = models.DateTimeField(auto_now_add=True, verbose_name="последняя попытка", **NULLABLE)
    server_response = models.CharField(verbose_name="ответ сервера", **NULLABLE)
    status = models.BooleanField(verbose_name="статус", **NULLABLE)

    def __str__(self):
        str = f'{self.mailing} {self.last_try} '
        if self.status:
            str += ' успешно отправилось'
        else:
            str += f' ошибка: {self.server_response}'
        return str

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"


