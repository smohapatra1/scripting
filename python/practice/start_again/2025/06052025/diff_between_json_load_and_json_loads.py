#   https://www.geeksforgeeks.org/python-difference-between-json-load-and-json-loads/

import json

data = {
    "name": "X",
    "place": "Y",
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "xyz@gmail.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
with open ('file.json', 'w') as f:
    json.dump(data, f)

with open('file.json', 'r') as f2:
    print (json.load(f2))
