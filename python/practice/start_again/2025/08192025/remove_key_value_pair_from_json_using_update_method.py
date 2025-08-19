#   https://www.geeksforgeeks.org/python/how-to-remove-key-value-pair-from-a-json-file-in-python/

import json
with open('file.json', 'r') as file:
    data = json.load(file)
key_to_remove = "featured_article"
if key_to_remove in data.keys():
    updated_data = {}
    for key, value in data.items():
        if key != key_to_remove:
            updated_data.update({key: value})
        else:
            removed_value = value
    print (f"Removed Key '{key_to_remove}' with value : {removed_value}")
else:
    print ("Key doesn't exist")

with open('output.json', 'w') as output:
    json.dump(updated_data, output , indent=2)