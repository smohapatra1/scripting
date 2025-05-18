#   https://www.geeksforgeeks.org/python-pretty-print-json/

import json 
with open('file.json', 'r') as f:
    obj = json.load(f)
    res = json.dumps(obj, indent=4)
    print (res)
