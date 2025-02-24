#   https://www.geeksforgeeks.org/write-a-dictionary-to-a-file-in-python/
import json

details = {'Name': "Bob", 
          'Age' :28} 

with open('file.txt', 'w') as f:
    f.write(json.dumps(details))