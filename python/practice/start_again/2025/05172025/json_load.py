#   https://www.geeksforgeeks.org/json-load-in-python/

import json
f = open('file.json')
data = json.load(f)
for i in data['details']:
    print (i)
f.close()