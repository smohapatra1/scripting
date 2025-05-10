#   https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/

import json
json_string = '{"Name": "Sam", "age": 20, "Course": "JSON"}'
dict = json.loads(json_string)
print (dict)