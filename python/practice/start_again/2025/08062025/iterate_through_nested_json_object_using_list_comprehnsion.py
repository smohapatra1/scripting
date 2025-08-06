#   https://www.geeksforgeeks.org/python/iterate-through-nested-json-object-using-python/

import json

def iterate_nested_json_list_comprehension(json_obj):
    items = [(key, value) if not isinstance(value, dict) else (key, iterate_nested_json_list_comprehension(value)) for key, value  in json_obj.items()]
    return items


nested_json = {
    "name" : "sam", 
    "age" : "30",
    "city" : "ba"
}

print ("\nUsing nested list comprehension")
result = iterate_nested_json_list_comprehension(nested_json)
print (result)