#   https://www.geeksforgeeks.org/python-pretty-print-json/

import json
data = [{"studentid": 1, "name": "ABC", 
         "subjects": ["Python", "Data Structures"]},
        {"studentid": 2, "name": "PQR", 
         "subjects": ["Java", "Operating System"]}]

with open('file3.json', 'w') as f:
    json.dump(data, f, indent=4)
f.close()