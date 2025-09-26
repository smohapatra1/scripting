#   https://www.geeksforgeeks.org/python/add-json-library-in-python/

import json
data = {"name": "GFG", "age": 1, "skills": [
    "writing", "coding", "answering questions"]}
json_string = json.dumps(data)
print (json_string)
new_data = json.loads(json_string)
print (new_data["name"])