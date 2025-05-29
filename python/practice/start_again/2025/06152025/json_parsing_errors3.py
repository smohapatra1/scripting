#   https://www.geeksforgeeks.org/json-parsing-errors-in-python/

import json

json_data = '{ "name": "xyz", "age": "twenty two" }'
try: 
    data = json.loads(json_data)
    age = int(data["age"])
    print (age)
except ValueError:
    print("'age' value is not a valid integer in JSON data")