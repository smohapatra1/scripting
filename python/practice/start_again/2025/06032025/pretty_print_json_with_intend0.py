#   https://www.geeksforgeeks.org/python-pretty-print-json/

import json
json_data = '[ {"studentid": 1, "name": "ABC", \
"subjects": ["Python", "Data Structures"]}, \
                {"studentid": 2, "name": "PQR",\
                "subjects": ["Java", "Operating System"]} ]'
obj = json.loads(json_data)
res = json.dumps(obj, indent=0)
print (res)