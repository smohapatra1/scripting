#   https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

import json

dictionary = {
    "name": "sam",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "92318716"
}

with open('sample2.json', 'w') as f:
    json.dump(dictionary, f, indent=4)
