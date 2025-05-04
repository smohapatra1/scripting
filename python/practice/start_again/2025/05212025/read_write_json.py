#   https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/

import json
emp ='{"id":"09", "name": "Sam", "department":"Finance"}'
emp_dict = json.loads(emp)
print (emp_dict)
print (emp_dict['name'])