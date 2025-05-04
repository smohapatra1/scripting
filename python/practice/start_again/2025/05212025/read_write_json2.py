#   https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/

import json

f = open('test1.json')
data = json.load(f)
for i in data['emp_details']:
    print (i)
f.close()