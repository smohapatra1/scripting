#   https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

import json
dictionary = {
    "name": "sam",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "92318716"
}

json_object = json.dumps(dictionary, indent=4)

with open("samaple.json", 'w') as f:
    f.write(json_object)