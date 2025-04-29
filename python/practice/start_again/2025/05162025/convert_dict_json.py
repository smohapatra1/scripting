#   https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/

import json

d = {"name": "sam", "age": "20"}

print (json.dumps(d, indent=4))
print (json.dumps(d, sort_keys=True))
print (json.dumps(d, ensure_ascii=False))
print (json.dumps([{k: d[k]} for k in d]))
