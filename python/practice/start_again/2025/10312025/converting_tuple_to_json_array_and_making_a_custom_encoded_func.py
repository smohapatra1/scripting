#   https://www.geeksforgeeks.org/python/convert-tuple-to-json-array-in-python/

import json

physics_tuple = ('Class 9', 'Physics', 'Laws of Motion', 'Introduction', 'Newton First Law')

def custom_encoder(obj):
    if isinstance(obj, tuple):
        return {'__tuple__': True, 'items': list(obj)}
    return obj
json_data = json.dumps(physics_tuple, default=custom_encoder)
print (type(json_data))
print (json_data)