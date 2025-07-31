#   https://www.geeksforgeeks.org/python/build-a-json-object-in-python/

import json
data = { "name": "sam", "age" : 9, "student": True}
json_string = json.dumps(data)
print (type(json_string))
print (json_string)