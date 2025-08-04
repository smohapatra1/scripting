#   https://www.geeksforgeeks.org/python/check-if-python-json-object-is-empty/

import json
def is_json_empty(json_obj):
    return json_obj == {}
json_obj = {}
# json_obj = [('name', 'Sam'), ('age', 29), ('is_student', True)]
print (is_json_empty(json_obj))