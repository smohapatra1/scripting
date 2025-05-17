#   https://www.geeksforgeeks.org/python-json/

import json
d = {'id': '09', 'name': 'Nitin', 'department': 'Finance'}
print("This is Python", type(d))
print("\nNow Convert from Python to JSON")

# Convert Python dict to JSON
obj = json.dumps(d, indent=4)
print("Converted to JSON", type(obj))
print(obj)