#   https://www.geeksforgeeks.org/serializing-json-data-in-python/

import json

data = {
    "user": {
        "name": "test x",
        "age": 21,
        "Place": "X",
        "Blood group": "O+"
    }
}
res = json.dumps(data)
print (res)