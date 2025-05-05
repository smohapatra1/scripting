#   https://www.geeksforgeeks.org/read-json-file-using-python/
import json

with open('file.json', 'r') as f:
    data = json.load(f)

print (data)