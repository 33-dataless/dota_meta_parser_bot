import pytz
import datetime

tz = pytz.timezone('Europe/Moscow')
def get_time_now() -> datetime.datetime:
    return datetime.datetime.now(tz)