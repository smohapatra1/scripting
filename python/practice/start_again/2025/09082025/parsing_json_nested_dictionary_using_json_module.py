#   https://www.geeksforgeeks.org/python/parsing-json-nested-dictionary-using-python/

import json

json_data = '{"name": "X", "age": 30, "address": {"city": "New York", "zipcode": "10001"}}'
parsed_data = json.loads(json_data)
print ('Name:', parsed_data['name'])
print ('Address', parsed_data['address']['city'])


