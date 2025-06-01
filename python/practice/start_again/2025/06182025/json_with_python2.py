#   https://www.geeksforgeeks.org/json-with-python/

import json
f = open('file.json',)
data = json.load(f)
for i in data:
    print (i)
f.close()