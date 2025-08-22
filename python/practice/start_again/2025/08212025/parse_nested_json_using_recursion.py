#   https://www.geeksforgeeks.org/python/how-to-parse-nested-json-in-python/

import json
# n_json = '{"name": "X", "age": 23, "address": {"city": "Y", "zipcode": "83625"}}'
n_json = '{"person": {"name": "X", "age": 23, "address": {"city": "y", "zipcode": "2123"}}}'

def parse_json(data):
    result = {}
    for key, val in data.items():
        if isinstance(val, dict):
            result[key] = parse_json(val)
        else:
            result[key] = val
    return result
data = parse_json(json.loads(n_json))
name = data['person']['name']
age = data['person']['age']
city = data['person']['address']['city']
zipc = data['person']['address']['zipcode']
print (f'Name: {name}')
print (f'Age: {age}')
print (f'Zipcode: {zipc}')