#   https://www.geeksforgeeks.org/how-to-fix-datetime-datetime-not-json-serializable-in-python/

import json
import datetime

def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")
dt = datetime.datetime.now()

json_data = json.dumps(dt, default=serialize_datetime)
print(json_data)