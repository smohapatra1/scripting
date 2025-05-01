#   https://www.geeksforgeeks.org/json-dumps-in-python/

import json

Dictionary ={(1, 2, 3):'Welcome', 2:'to',
            3:'Sams', 4:'coding',
            5:'Hah ha ha '}
json_string = json.dumps(Dictionary, 
                         skipkeys = True)
print('Equivalent json string of dictionary:', 
      json_string)