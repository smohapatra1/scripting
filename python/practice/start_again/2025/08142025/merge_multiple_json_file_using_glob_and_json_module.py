#   https://www.geeksforgeeks.org/python/how-to-merge-multiple-json-files-using-python/

import json 
import glob

def merged_json_files(directory_path):
    merged_data = []
    file_paths = glob.glob(directory_path + '/*.json')
    for path in file_paths:
        with open(path, 'r') as file:
            data = json.load(file)
            merged_data.append(data)
    return merged_data

directory_path = "./files"
output_file = "merged.json"
merged_data = merged_json_files(directory_path)
with open(output_file, 'w') as out:
    json.dump(merged_data, out)
print (merged_data)