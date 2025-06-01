#   https://www.geeksforgeeks.org/json-with-python/

import json

# Data to be written
dictionary ={
    "name" : "N",
    "rollno" : 420,
    "cgpa" : 10.10,
    "phonenumber" : "1234567890"
}

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)