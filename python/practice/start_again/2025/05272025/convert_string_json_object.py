#   https://www.geeksforgeeks.org/python-ways-to-convert-string-to-json-object/

import json

name = '{"Name": "sam", "age" : 20, "course": "read"}'
res = json.loads(name)
print (type(res), res)