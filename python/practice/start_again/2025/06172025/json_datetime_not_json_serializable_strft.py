# https://www.geeksforgeeks.org/how-to-fix-datetime-datetime-not-json-serializable-in-python/

import json 
import datetime

dt = datetime.datetime.now()
dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
json_data = json.dumps(dt_str)
print(json_data)