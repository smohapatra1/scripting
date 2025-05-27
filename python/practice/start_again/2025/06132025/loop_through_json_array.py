#   https://www.geeksforgeeks.org/loop-through-a-json-array-in-python/

import json
json_data = """
[
    {"id":  1, "name": "John"},
    {"id":  2, "name": "Jane"},
    {"id":  3, "name": "Bob"}
]
"""
data = json.loads(json_data)

for item in data:
    print(item["id"], item["name"])