import pytz
from django.utils import timezone


def convert_to_localtime(utctime):
    fmt = '%d/%m/%Y %H:%M'
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz.strftime(fmt)
