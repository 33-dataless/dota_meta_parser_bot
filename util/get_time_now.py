import pytz
import datetime

tz = pytz.timezone('Europe/Moscow')

def get_time_now(format_file=False) -> datetime.datetime:
    now = datetime.datetime.now(tz)
    if format_file:
        return now.strftime("%d_%m_%y")
    return now.strftime("%d:%m:%y | %H:%M")

