#   https://www.geeksforgeeks.org/python-json/

import json
json_data = '[ {"studentid": 1, "name": "ABC", \
"subjects": ["Python", "Data Structures"]}, \
                {"studentid": 2, "name": "PQR",\
                "subjects": ["Java", "Operating System"]} ]'
obj = json.loads(json_data)
print (obj)
res = json.dumps(obj, indent=4)
print (res)