#   https://www.geeksforgeeks.org/python/check-if-python-json-object-is-empty/

import json

def is_json_empty(json_obj):
    return len(json_obj) ==0 
json_obj = {}

print (is_json_empty(json_obj))
