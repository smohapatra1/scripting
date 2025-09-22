#   https://www.geeksforgeeks.org/python/update-json-key-name-in-python/

original_json = {'old_key1': 'value1', 'old_key2': 'value2'}
key_mapping = {'old_key1': 'new_key1', 'old_key2': 'new_key2'}
updated_json = {key_mapping.get(key, key): value for key, value in original_json.items()}
print (updated_json)