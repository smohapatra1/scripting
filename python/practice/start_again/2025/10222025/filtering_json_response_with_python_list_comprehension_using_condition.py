#   https://www.geeksforgeeks.org/python/filtering-json-response-with-python-list-comprehension/

import json

json_response = '[{"name": "John", "age": 25}, {"name": "Jane", "age": 35}, {"name": "Bob", "age": 28}]'
data = json.loads(json_response)
filtered_data = [item for item in data if item["age"] > 30 ]
print (filtered_data)
