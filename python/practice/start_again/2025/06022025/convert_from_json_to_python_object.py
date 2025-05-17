#   https://www.geeksforgeeks.org/python-json/

import json
emp = '{"id":"09", "name": "Sam", "department":"eng"}'
print ("this is Json" , type(emp))
print("\nNow convert from JSON to Python")

d= json.loads(emp)
print ("Converted to Python", type(d))
print (d)