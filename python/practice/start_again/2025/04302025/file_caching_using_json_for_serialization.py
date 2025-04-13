#   https://www.geeksforgeeks.org/how-to-implement-file-caching-in-python/

import json

file_cache = {}
def read_file_json(file_path):
    if file_path not in file_cache:
        with open(file_path, 'r') as file:
            file_content = json.load(file)
            file_cache[file_path] = file_content
    return file_cache[file_path]

data = {'website': 'wich.com'}
with open('file.json', 'w') as file2:
    json.dump(data, file2)
result = read_file_json('file.json')
print (result)

