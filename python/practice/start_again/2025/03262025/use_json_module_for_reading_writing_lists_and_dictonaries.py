#   https://www.geeksforgeeks.org/reading-and-writing-lists-to-a-file-in-python/

import json

config_data = {
    'name': 'John',
    'role': 'developer',
    'languages': ['Python', 'JavaScript']
}
config_File = 'config.json'
with open(config_File, 'w') as config_file:
    json.dump(config_data, config_file)
print(f'The last has been written to file {config_File}.')