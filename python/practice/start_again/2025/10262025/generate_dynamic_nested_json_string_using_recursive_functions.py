#   https://www.geeksforgeeks.org/python/python-to-generate-dynamic-nested-json-string/

import json

def convert_to_json(obj):
    if isinstance(obj, dict):
        return {key: convert_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_json(item) for item in obj]
    else:
        return obj

data_recursive = {
    "name": "Alice",
    "age": 28,
    "address": {"city": "Villageaaaatown", "zip": "67890"},
    "contacts": [{"type": "email", "value": "alice@example.com"}]
}
json_recursive = json.dumps(convert_to_json(data_recursive), indent=2)
print (json_recursive)
