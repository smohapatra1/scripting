#   https://www.geeksforgeeks.org/python/how-to-merge-multiple-json-files-using-python/

import json

def merge_json_files(file_paths, output_file):
    merged_data = []
    for path in file_paths:
        with open (path, 'r') as file:
            data = json.load(file)
            merged_data.append(data)
    with open(output_file, 'w') as outputfile:
        json.dump(merged_data, outputfile)

file_paths = ["file.json", "file3.json"] 
output_file = "merged_json"
merge_json_files(file_paths, output_file)
print (f"Merged written to '{output_file}")
