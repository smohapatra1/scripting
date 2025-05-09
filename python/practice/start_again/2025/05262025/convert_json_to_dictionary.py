#   https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/

import json

jsonString = '{ "id": 121, "name": "Sam", "course": "Mem Cache"}'
student = json.loads(jsonString)
print (student)
print (student['name'])
print (student['id'])