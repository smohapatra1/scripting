#   https://www.geeksforgeeks.org/python/extract-multiple-json-objects-from-one-file-using-python/

import json
extracted_objs = []
with open('file.json', 'r') as f:
    for line in f:
        json_obj = json.loads(line)
        extracted_objs.append(json_obj)
print (extracted_objs)