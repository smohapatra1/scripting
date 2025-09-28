#   https://www.geeksforgeeks.org/python/create-a-json-representation-of-a-folder-structure/

import os 
import json

def create_folder(path):
    result = {'name': os.path.basename(path),
              'type': 'folder', 'children': []}
    if not os.path.isdir(path):
        return result
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            result['children'].append(create_folder(entry_path)) 
        else:
            result['children'].append({'name': entry, 'type': 'file'})
    return result
folder_path = 'test/2025'
folder_json = create_folder(folder_path)
folder_json_string = json.dumps(folder_json, indent=4)
print (folder_json_string)