import json
from datetime import datetime, time, date

dict_with_times = {
    'date': date(2023, 9, 2),
    'datetime': datetime(2023, 9, 2, 15, 30, 0),
    'time': time(15, 30, 19),
}

def json_serial(obj):

    if isinstance(obj, (datetime, date, time)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


print(json.dumps(dict_with_times, default=json_serial))