#   https://www.geeksforgeeks.org/python/iterate-through-nested-json-object-using-python/

import json

def iterate_nested_json_flatten(json_obj):
    flattened_json_str = json.dumps(json_obj)
    flattened_json = json.loads(flattened_json_str)
    for key, value in flattened_json.items():
        print (f"{key}: {value}")
nested_json = {
    "name": "sam",
    "age" : "20",
    "address": {
        "city": "ba",
        "zip" : "1234"
    }

}
print ("Using json.dumps")
iterate_nested_json_flatten(nested_json)
