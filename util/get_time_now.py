import pytz
import datetime

tz = pytz.timezone('Europe/Moscow')

def get_time_now() -> datetime.datetime:
    now = datetime.datetime.now(tz)
    return now.strftime("%d:%m:%y | %H:%M")

