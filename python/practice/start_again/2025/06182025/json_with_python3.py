#   https://www.geeksforgeeks.org/json-with-python/

import json

dictionary = {
    "name": "sam",
    "department": "HR",
    "Company": 'GFG'
}
json_object = json.dumps(dictionary)
print(json_object)