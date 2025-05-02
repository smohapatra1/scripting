#   https://www.geeksforgeeks.org/python-convert-json-to-string/

import json

a = {"name" : "Reading", "Topic" : "Json to String", "Method": 1}
y = json.dumps(a)
print (y)
print (type(y))