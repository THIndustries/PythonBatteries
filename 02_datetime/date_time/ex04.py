from datetime import datetime

from datetime import datetime


def convert_str_to_datetime(date_str):
    format_str = "%b %d %Y %I:%M %p"
    date_time_obj = datetime.strptime(date_str, format_str)

    year = date_time_obj.year
    mount = date_time_obj.month
    day = date_time_obj.day
    hour = date_time_obj.hour
    minute = date_time_obj.minute
    return datetime(year, mount, day, hour, minute)




assert convert_str_to_datetime('Jul 1 2014 2:43 PM') == datetime(2014, 7, 1, 14, 43)
assert convert_str_to_datetime('Aug 18 2005 6:00 AM') == datetime(2005, 8, 18, 6, 0)
assert convert_str_to_datetime('Dec 31 2020 11:59 PM') == datetime(2020, 12, 31, 23, 59)
assert convert_str_to_datetime('Feb 29 2012 09:29 PM') == datetime(2012, 2, 29, 21, 29)