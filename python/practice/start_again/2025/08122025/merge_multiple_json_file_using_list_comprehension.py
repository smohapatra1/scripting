#   https://www.geeksforgeeks.org/python/how-to-merge-multiple-json-files-using-python/

import json
def merge_json_file(file_paths):
    merged_data = [json.load(open(path, 'r')) for path in file_paths]
    return merged_data

file_paths = ["f.json", "s.json", "e.json", "t.json"]
output_file = "merged.json"
merged_data = merge_json_file(file_paths)
with open(output_file, 'w') as outputfile:
    json.dump(merged_data, outputfile) 
print (merged_data)