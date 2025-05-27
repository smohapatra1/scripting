#   https://www.geeksforgeeks.org/loop-through-a-json-array-in-python/

import json

json_data = """
{
    "sample_data": [
        {"id": 1, "name": "x"},
        {"id": 2, "name": "Y"},
        {"id": 3, "name": "Z"}
    ]
}
"""
data = json.loads(json_data)
for item in data["sample_data"]:
    print (item["id"], item["name"])
