#   https://www.geeksforgeeks.org/how-to-fix-datetime-datetime-not-json-serializable-in-python/

import json
import datetime

now = datetime.datetime.now()
json.dumps(now)