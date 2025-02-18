#   https://www.geeksforgeeks.org/write-a-dictionary-to-a-file-in-python/

import json
details = {'name' : "Bob", 'Age': 28}
with open('convert.txt', 'w') as file:
    file.write(json.dumps(details))