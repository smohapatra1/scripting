#   https://www.geeksforgeeks.org/loop-through-a-json-array-in-python/

import json

with open("file.json") as f:
    data = json.load(f)

for item in data:
    print (item["id"], item["name"])