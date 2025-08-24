#   https://www.geeksforgeeks.org/python/modify-json-fields-using-python/

import json
json_data = '{"name": "Alice", "age": 30, "city": "Los Angeles"}'
data = json.loads(json_data)
field_key = 'age'
if field_key in data:
    data[field_key] +=1

modified_json = json.dumps(data)
print ("Before Modifying :", json_data)
print ("After Modifying  : ", modified_json)