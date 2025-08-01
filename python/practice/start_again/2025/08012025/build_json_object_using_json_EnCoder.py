#   https://www.geeksforgeeks.org/python/build-a-json-object-in-python/

import json

def encoder(obj):
    if isinstance(obj, set):
        return list(obj)
    return obj

gfg = [('name', 'Sam'), ('age', 29), ('is_student', True)]
json_data = dict(gfg)
json_string = json.dumps(json_data, default=encoder)
print (type(json_string))
print (json_string)