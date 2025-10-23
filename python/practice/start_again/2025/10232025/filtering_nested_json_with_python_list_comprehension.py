#   https://www.geeksforgeeks.org/python/filtering-json-response-with-python-list-comprehension/

import json

json_response = '{"person": {"name": "John", "address": {"city": "New York", "zip": "10001"}}}'
data = json.loads(json_response)
filtered_data = {key: data["person"] ["address"][key] for key in data["person"]["address"] if key == "city"}
print (filtered_data)