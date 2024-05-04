from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.utils import timezone
from django_apscheduler.jobstores import DjangoJobStore

from main.models import Mailing
from main.services import start_mailing


def filter_mailing(mailing):
    now = timezone.localtime(timezone.now())
    if mailing.start < now < mailing.finish:

        if not mailing.next_sending_time:
            if mailing.date_time >= now:
                mailing.next_sending_time = mailing.date_time
            else:
                if now.time() > mailing.date_time.time():
                    mailing.next_sending_time = datetime.combine(
                        now.date() + timedelta(days=1), mailing.date_time.time()
                    )
                mailing.next_sending_time = datetime.combine(now.date(), mailing.date_time.time())
            mailing.save()

        elif now > mailing.next_sending_time > mailing.start:
            start_mailing(mailing)
            mailing.status = "Выполняется"
            mapa = {"День": 1, "Неделя": 7, "Месяц": 30}
            mailing.next_sending_time = now + timedelta(days=mapa[mailing.period])

            mailing.save()

    elif now > mailing.finish:
        mailing.status = "Завершена"
        mailing.save()


def sending_tasks():

    mailings = Mailing.objects.filter(status__in=["Создана", "Выполняется"])
    if mailings.exists():
        for mailing in mailings:
            if mailing.is_active:
                filter_mailing(mailing)


def start_scheduler():
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")
    print("Starting scheduler...")

    scheduler.add_job(
        sending_tasks, trigger=CronTrigger(minute="*/1"), id="sending_tasks", max_instances=1, replace_existing=True
    )

    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown(wait=False)
