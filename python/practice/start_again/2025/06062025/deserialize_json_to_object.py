#   https://www.geeksforgeeks.org/deserialize-json-to-object-in-python/

import json

data = '{"Name" : "Romy", "Gender" : "Female"}'
print ("Datatypes before deserialization : " + str(type(data)))
data = json.loads(data)
print ("Datatypes after deserialization : " + str(type(data)))