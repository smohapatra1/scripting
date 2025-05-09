#   https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/

import json
with open('file.json') as f:
    data = json.load(f)
    print (data['people1'][0])