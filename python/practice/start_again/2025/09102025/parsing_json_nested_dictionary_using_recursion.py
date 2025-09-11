#   https://www.geeksforgeeks.org/python/parsing-json-nested-dictionary-using-python/

import json
json_data = {"name": "John", "age": 30, "address": {"city": "New York", "zipcode": "10001"}}
keys_to_extract = ['address', 'city']
def recursive(data, keys):
    if not keys:
        return data
    return recursive(data.get(keys[0], {}), keys[1:])
result = recursive(json_data, keys_to_extract)
print ('City: ', result)