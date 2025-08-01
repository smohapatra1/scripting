#   https://www.geeksforgeeks.org/python/build-a-json-object-in-python/

import json

data = '{ "name": "sam", "age" : 9, "student": true}'
data1 = json.loads(data)
print (type(data))
print (data1)