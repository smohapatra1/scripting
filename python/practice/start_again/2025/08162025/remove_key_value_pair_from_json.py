#   https://www.geeksforgeeks.org/python/how-to-remove-key-value-pair-from-a-json-file-in-python/

import json
with open('file.json', 'r') as file:
    data = json.load(file)
key_to_remove = 'featured_article'
if key_to_remove in data:
    removed_value = data.pop(key_to_remove)
    print (f"Removed Key '{key_to_remove}' with value {removed_value}" )
with open('output.json', 'w') as file:
    json.dump(data, file, indent=2)

