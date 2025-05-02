#   https://www.geeksforgeeks.org/json-dumps-in-python/

import json

Dictionary ={'c':'Welcome', 'b':'to',
            'a':'Samar'}
json_string = json.dumps(Dictionary, 
                         indent = 6,
                         separators=(". ", " =  "),
                         sort_keys= True)
print ("Equivalent json string to dictionary ", json_string)