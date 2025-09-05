#   https://www.geeksforgeeks.org/python/extract-multiple-json-objects-from-one-file-using-python/

import re 
import json
pattern = r'{.*}'

with open('file.json', 'r') as f:
    file_count = f.read()
json_objs = re.findall(pattern, file_count)

for obj_string in json_objs:
    obj = json.loads(obj_string)
    print (obj)