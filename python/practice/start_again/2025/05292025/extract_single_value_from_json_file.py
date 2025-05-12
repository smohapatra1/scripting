#   https://www.geeksforgeeks.org/python-program-to-extract-a-single-value-from-json-response/

import json

with open('file.json', 'r') as f:
    value = json.load(f)
test = value['emp_name']
test1 = test[1].values()
test2 = list(test1)[0]
test3 = test2[1:-1].split(',')
print (test3[1])