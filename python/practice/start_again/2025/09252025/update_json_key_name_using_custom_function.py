#   https://www.geeksforgeeks.org/python/update-json-key-name-in-python/

import json 

def update_json_keys(data, old_keys, new_keys):
    for old_key, new_key in zip(old_keys, new_keys):
        if old_key in data:
            data[new_key] = data.pop(old_key)
original = {'old_key1': 'value1', 'old_key2' : 'value2'}
update_json_keys(original, ['old_key1', 'old_key2'], ['new_key1', 'new_key2'])
print (original)