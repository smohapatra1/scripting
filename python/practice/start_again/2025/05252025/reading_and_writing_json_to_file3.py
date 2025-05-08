#   https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

import json

with open('file.json', 'r') as f:
    json_obj =json.load(f) 

print (json_obj)