#   https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/

import json
d = {"name": "sam", "age": 21, "address": {"city": "Ind"}}

print(json.dumps(d, indent=4))                   # Pretty print JSON
print(json.dumps(d, sort_keys=True, indent=4))   # Sorted keys
print(json.dumps(d, ensure_ascii=False, indent=4))  # Non-ASCII encoding
print(json.dumps([{k: d[k]} for k in d], indent=4))  # Convert to JSON array format