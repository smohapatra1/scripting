#   https://www.geeksforgeeks.org/python/check-if-json-object-has-empty-value-in-python/

import json
json_data = '{"name": "John", "age": 25, "city": "", "email": null}'
parsed_json = json.loads(json_data)
empty_values = [ not value for value in parsed_json.values()]
result = any(empty_values)
print (f"Does this JSON object have empty values ? {result}")