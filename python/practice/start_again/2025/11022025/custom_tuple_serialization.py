#   https://www.geeksforgeeks.org/python/convert-tuple-to-json-array-in-python/

import json

physics_tuple = ('Class 9', 'Physics', 'Laws of Motion', 'Introduction', 'Newton First Law')

def serialization(obj):
    if isinstance(obj, tuple):
        return {'tuple_items': list(obj)}
    return obj
json_data = json.dumps(physics_tuple, default=serialization)
print (json_data)