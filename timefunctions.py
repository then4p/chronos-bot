import datetime
from dateutil.parser import parse
from dateutil.tz import *

# add new timezones here
TIMEZONES = {'SET': gettz('America/New_York'),
             'GMT': gettz('Europe/London'),
             'CET': gettz('Europe/Berlin')}


# parses time and ignores the rest of the string, returns a datetime object
def parser(time):
    return parse(time, tzinfos=TIMEZONES, fuzzy=True)


# converts the timefrom the message into UTC for further manipulation
def normalize(time):
    return time


# returns a timedelta object
def delta(time):
    return time - datetime.datetime.now(TIMEZONES['CET'])


def print(time):
    return time.strftime("%H:%M", time)
