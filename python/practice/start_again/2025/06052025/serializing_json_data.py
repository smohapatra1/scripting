#   https://www.geeksforgeeks.org/serializing-json-data-in-python/

import json
data = {
    "user": {
        "name": "sam kumar",
        "age": 21,
        "Place": "Xyz",
        "Blood group": "O+"
    }
}
with open('file.json', 'w') as f:
    json.dump(data, f)