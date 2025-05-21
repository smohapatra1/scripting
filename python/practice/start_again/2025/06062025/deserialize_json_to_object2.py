#   https://www.geeksforgeeks.org/deserialize-json-to-object-in-python/

import json

data = open('file.json',) 
print ("Datatypes before deserialization : " + str(type(data)))
data = json.load(data)
print ("Datatypes after deserialization : " + str(type(data)))