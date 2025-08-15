#   https://www.geeksforgeeks.org/python/how-to-merge-multiple-json-files-using-python/

import pandas as pd 
import json

def merge_json_files(file_path):
    merged_data = pd.DataFrame()
    for path in file_path:
        with open(path, 'r') as file:
            data = json.load(file)
            row = pd.DataFrame([data])
            merged_data = pd.concat([merged_data, row], ignore_index=True)
    return merged_data

file_paths = ['file.json', 'file3.json']
output_file = "merged_json"
merged_data = merge_json_files(file_path)
merged_data.to_json(output_file, orient='records')
print (merged_data)