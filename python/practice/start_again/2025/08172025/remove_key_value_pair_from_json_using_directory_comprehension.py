#   https://www.geeksforgeeks.org/python/how-to-remove-key-value-pair-from-a-json-file-in-python/

import json
with open('file.json', 'r') as file:
    data = json.load(file)
key_to_remove = "featured_article"

if key_to_remove in data.keys():
    updated_data = {key: value for key, value in data.items() if key != key_to_remove}
    removed_value = data[key_to_remove]
    print (f"Removed key '{key_to_remove}' with value: {removed_value}")
else:
    print ("Key doesn't exist")

with open('ouput.json', 'w') as f:
    json.dump(updated_data, f, indent=2)
