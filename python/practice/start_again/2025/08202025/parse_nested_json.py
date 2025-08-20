#   https://www.geeksforgeeks.org/python/how-to-parse-nested-json-in-python/

import json
n_json = '{"name": "X", "age": 23, "address": {"city": "Y", "zipcode": "83625"}}'
data = json.loads(n_json)
name = data['name']
age = data['age']
city = data['address']['city']
zip = data['address']['zipcode']
print (f"Name: {name}")
print (f"Age: {age}")
print (f"City: {city}")
print (f"Zip: {zip}")

