#   https://www.geeksforgeeks.org/python/single-vs-double-quotes-in-python-json/

import json

json_data_double = '{"name": "Sam", "age" : "20", "city" : "usa"}'
parsed = json.loads(json_data_double)
print ("Using double quotes")
print (parsed)