#   https://www.geeksforgeeks.org/python/check-if-json-object-has-empty-value-in-python/

import json

json_data = '{"name": "John", "age": 25, "city": "", "email": null}'
parsed_json = json.loads(json_data)
for key, value in parsed_json.items():
    if not value:
        print (f"Empty value found for key: {key}")
