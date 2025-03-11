#   https://www.geeksforgeeks.org/reading-and-writing-lists-to-a-file-in-python/

import json

with open('config.json', 'r') as f:
    config_data = json.load(f)
print(config_data)