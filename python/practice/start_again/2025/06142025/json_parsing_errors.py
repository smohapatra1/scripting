#   https://www.geeksforgeeks.org/json-parsing-errors-in-python/

import json
json_data = '{ "name": "Om Mishra", "age": 22, "city": "Ahmedabad" '  
try:
    data = json.loads(json_data)
    print (data)
except json.JSONDecodeError as e:
    print ("invalid JSON syntax", e)