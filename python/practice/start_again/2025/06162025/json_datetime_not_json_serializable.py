#   https://www.geeksforgeeks.org/how-to-fix-datetime-datetime-not-json-serializable-in-python/

import json

data = {
    "name": "Smith",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "phoneNumbers": [
        {"type": "home", "number": "555-555-5555"},
        {"type": "work", "number": "555-555-5555"}
    ]
}
json_data = json.dumps(data)
print (json_data)