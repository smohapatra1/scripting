#   https://www.geeksforgeeks.org/built-in-modules-in-python/

import json 

data = {
    "name": "Sam",
    "age": 30,
    "is_student": True,
    "courses": ["Web Dev", "CP"]
}

json_string = json.dumps(data, indent=4)
print (json_string)