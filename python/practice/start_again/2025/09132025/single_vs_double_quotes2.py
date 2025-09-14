#   https://www.geeksforgeeks.org/python/single-vs-double-quotes-in-python-json/

import json
mixed_quote_data ={
    'name': "John",
    "age": 30,
    'city': 'New York',
    "is_student": False,
    "grades": {
        "math": 95,
        'history': 87,
        "english": 92
    }
}
json_data = json.dumps(mixed_quote_data, indent=2)

print (json_data)