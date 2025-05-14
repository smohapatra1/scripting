#   https://www.geeksforgeeks.org/how-to-return-a-json-object-from-a-python-function/

import json
def test():
    value = {
        "firstName": "a",
        "lastName": "b",
        "hobbies": ["playing", "problem solving", "coding"],
        "age": 20,
        "children": [
            {
                "firstName": "x",
                "lastName": "y",
                "age": 15
            },
            {
                "firstName": "s",
                "lastName": "t",
                "age": 18
            }
        ]
    }
    return json.dumps(value)
print (test())