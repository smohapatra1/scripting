#   https://www.geeksforgeeks.org/json-parsing-errors-in-python/

import json
json_data = '{ "numbers": [1, 2, 3, 4, "5"] }' 
data = json.loads(json_data)
numbers = data["numbers"]
try:
    total = sum(numbers)
    print (total)
except TypeError:
    print ("Mismatch type detected")