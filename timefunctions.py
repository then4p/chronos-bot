import datetime
from dateutil.parser import parse
from dateutil.tz import *

TZOFFSETS = {"PH":gettz("America/New_York")}

def parse_time(time):
    return parse(time, tzinfos = TZOFFSETS,  fuzzy = True)

def countdown(time):
    return time.timedelta(time.gmtime(),time)

def print_time(time):
    return time.strftime("%H:%M", time)

