#   https://www.geeksforgeeks.org/python/extract-multiple-json-objects-from-one-file-using-python/

import json
custom_sep = ';'
with open('file.txt', 'r') as f:
    file_content = f.read()
    objects = file_content.split(custom_sep)
    for obj_str in objects:
        obj = json.loads(obj_str)
    print (obj) 