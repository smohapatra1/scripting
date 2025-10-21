#   https://www.geeksforgeeks.org/python/filtering-json-response-with-python-list-comprehension/

import json

json_response = '{"name": "John", "age": 25, "city": "New York", "gender": "male"}'
data = json.loads(json_response)

filtered_data = {key: value for key, value in data.items() if key in ["name", "age"]}
print(filtered_data)
