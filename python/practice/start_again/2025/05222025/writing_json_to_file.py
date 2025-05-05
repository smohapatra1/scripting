#   https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/

import json


dictionary ={
    "name" : "sam",
    "rollno" : 20,
    "cgpa" : 10.1,
    "phonenumber" : "xxxx1231"
}
with open("test3.json", "w") as f:
    json.dump(dictionary, f)