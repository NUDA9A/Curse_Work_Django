import smtplib
from datetime import datetime

import pytz
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail

from blogs.models import Blog
from main.models import Client
from main.models import Try
from main.models import Mailing


def start_mailing(mailing):
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone)
    try:
        send_mail(
            subject=mailing.message.title,
            message=mailing.message.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=list(mailing.clients.all().values_list("email", flat=True)),
            fail_silently=False,
        )
        Try.objects.create(status=True, mailing=mailing, last_try=now)
    except smtplib.SMTPException as e:
        Try.objects.create(status=False, mailing=mailing, last_try=now)


def get_cached_mailing_ammount():
    if settings.CACHE_ENABLED:
        key = "mailings_ammount"
        mailings_ammount = cache.get(key)
        if mailings_ammount is None:
            mailings_ammount = Mailing.objects.all().count()
            cache.set(key, mailings_ammount)
    else:
        mailings_ammount = Mailing.objects.all().count()
    return mailings_ammount


def get_cached_mailing_active():
    if settings.CACHE_ENABLED:
        key = "active_mailings_ammount"
        active_mailings_ammount = cache.get(key)
        if active_mailings_ammount is None:
            active_mailings_ammount = Mailing.objects.filter(is_active=True).count()
            cache.set(key, active_mailings_ammount)
    else:
        active_mailings_ammount = Mailing.objects.filter(is_active=True).count()
    return active_mailings_ammount


def get_cached_blog_list():
    if settings.CACHE_ENABLED:
        key = 'blogs'
        blogs = cache.get(key)
        if blogs is None:
            blogs = list(Blog.objects.filter(is_published=True))
            cache.set(key, blogs)
    else:
        blogs = list(Blog.objects.filter(is_published=True))
    return blogs


def get_cached_clients_ammount():
    if settings.CACHE_ENABLED:
        key = "clients_ammount"
        clients_ammount = cache.get(key)
        if clients_ammount is None:
            clients_ammount = Client.objects.distinct().count()
            cache.set(key, clients_ammount)
    else:
        clients_ammount = Client.objects.distinct().count()
    return clients_ammount
