#   https://www.geeksforgeeks.org/python/how-to-merge-multiple-json-files-using-python/

import os 
import json

def merge_two_json(directory_path):
    merged_data = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            with open(os.path.join(directory_path, filename), 'r') as file:
                data = json.load(file)
                merged_data.append(data)
    return merged_data
directory_path = "./file"
output_file = "test.json"
merged_data = merge_two_json(directory_path)
with open(output_file, 'w') as outputfile:
    json.dump(merged_data, outputfile)
print (merged_data)
