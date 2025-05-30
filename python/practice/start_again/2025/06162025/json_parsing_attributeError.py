#   https://www.geeksforgeeks.org/json-parsing-errors-in-python/

import json
json_data = '{ "person": { "name": "SAM", "age": 30 } }'

try:
    data = json.loads(json_data)
    name = data['person'].name
    print (name)
except AttributeError:
    print ("Invalid key in JSON data. Expected 'name' key to present ")