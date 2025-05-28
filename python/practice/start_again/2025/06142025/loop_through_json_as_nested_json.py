#   https://www.geeksforgeeks.org/loop-through-a-json-array-in-python/

import json

data = [
    {
        "nested_array": [
            {
                "value": "1"
            },
            {
                "value": "2"
            },
            {
                "value": "3"
            }
        ]
    },
    {
        "nested_array": [
            {
                "value": "4"
            },
            {
                "value": "5"
            },
            {
                "value": "6"
            }
        ]
    }
]

for item in data:
    for subitem in item["nested_array"]:
        print (subitem["value"])