#   https://www.geeksforgeeks.org/json-with-python/

import json

employee ='{"name": "Sam", "department":"Finance", "company":"GFG"}'

employee_dict = json.loads(employee)

print("Data after conversion")
print(employee_dict)
print(employee_dict['department'])

print("\nType of data")
print(type(employee_dict))