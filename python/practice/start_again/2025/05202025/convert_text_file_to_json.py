#   https://www.geeksforgeeks.org/convert-text-file-to-json-in-python/

import json

filename = 'file.txt'

dict1 = {}
with open(filename) as f:
    for line in f:
        command, description = line.strip().split(None, 1)
        dict1[command] = description.strip()

out_file = open('test1.json', 'w')
json.dump(dict1, out_file, indent=4, sort_keys=False)
out_file.close()