#   https://www.geeksforgeeks.org/json-parsing-errors-in-python/

import json

json_data = '{ "name": "Om Mishra", "age": 22 }' 
try : 
    data = json.loads(json_data)
    city = data["city"]
    print (city)
except KeyError:
    print ("Missing 'city' key in json file")