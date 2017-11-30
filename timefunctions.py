import datetime
from dateutil.parser import parse

def parse_time(time):
    return parse(time)

def countdown(time):
    return time.timedelta(time.gmtime(),time)

def print_time(time):
    return time.strftime("%H:%M", time)

