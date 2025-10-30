#   https://www.geeksforgeeks.org/python/convert-tuple-to-json-array-in-python/

import json
physics_tuple = ('Class 9', 'Physics', 'Laws of Motion', 'Introduction', 'Newton First Law')

json_data = json.dumps(physics_tuple)

print (type(json_data))
print (json_data)